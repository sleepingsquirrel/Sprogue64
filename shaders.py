

class shader_storage:
    vert_wall = '''
    #version 330
    in vec2 apos;
    out vec2 tex;
    void main()
    {
        gl_Position = vec4(apos, 0.1, 1);
        tex = (apos + 1) / 2;
    }
    '''
    frag_wall = '''
    #version 330
    #define W 500
    #define H 500
    out vec4 FragColor;
    in vec2 tex;
    uniform vec2 ppos;
    uniform float rot;
    uniform int w;
    uniform int h;
    uniform bool titleon;
    uniform float framecount;
    uniform sampler2D title;
    uniform sampler2D atlas;
    const float fov = 1.0;

    vec2 hash22(vec2 p)
    {
        p = p*mat2(127.1,311.7,269.5,183.3);
        p = -1.0 + 2.0 * fract(sin(p)*43758.5453123);
        return sin(p*6.283);
    }
    bool xor(bool a, bool b) {
        if ((a && b) || (!a && !b)) return false;
        else return true;
    }
    void main()
    {
        if (titleon){
            FragColor = texture(title, vec2(tex.x,1.0 - tex.y));
            return;
        }
        //FragColor = vec4(texture(atlas, tex));
        vec4 dat = texture(atlas, tex);
        if (dat.r / 2 > (abs(tex.y - 0.5))) {
            FragColor = vec4(dat.yzw,1.0);
        }
        else {
            float dif = -1.0/50000.0;
            if (tex.x > 0.5){
                dif = 0;
            }
            if (tex.y + dif <= 0.5){
                FragColor = vec4(1.0,1.0,1.0,1.0);
            }
            else{
                vec2 rand = hash22(vec2(round((tex.x+rot)*w)/w,round((tex.y)*h)/h));
                vec3 col = vec3(0);
                if (rand.x > 0.999){
                    //hash22(vec2(coord.x + rot + floor(hash22(coord).x + float(framecount) / 100.0), coord.y)).y;
                    col = vec3(hash22(vec2(rand.y)).x);
                }
                FragColor = vec4(vec3(col),1.0);
            }
        }
    } 
    '''
    frag_player = '''
    #version 330
    out vec4 FragColor;
    uniform sampler2D atlas;
    in vec2 texcoord;

    void main() {
        vec4 colour = texture(atlas, texcoord);
        FragColor = colour;
    }
    '''

    vert_entity = '''
    #version 330
    in vec2 tex;
    uniform vec2 tex_;
    out vec2 texloc;
    void main()
    {
        gl_Position = vec4(vec2(0,0) - 0.5, 0.1, 1);
        texloc = tex + tex_;
    }
    '''
    geo_entity  = '''
    #version 330 core
    layout (points) in;
    layout (triangle_strip, max_vertices = 6) out;
    uniform vec2 len_atlas;
    uniform vec2 scale;
    uniform vec3 pos;
    in vec2 texloc[];
    out float texcoord[5];
    void main()
    {
        gl_Position = vec4(1.0, 1.0, 0.0, 0.0);
        texcoord = vec4(1,1,texloc[0]);
        EmitVertex();
        gl_Position = vec4(0.0, 1.0, 0.0, 0.0);
        texcoord = vec4(0,1,texloc[0]);
        EmitVertex();
        gl_Position = vec4(0.0, 0.0, 0.0, 0.0);
        texcoord = vec4(0,0,texloc[0]);
        EmitVertex();
        gl_Position = vec4(1.0, 1.0, 0.0, 0.0);
        texcoord = vec4(1,1,texloc[0]);
        EmitVertex();
        gl_Position = vec4(1.0, 0.0, 0.0, 0.0);
        texcoord = vec4(1,0,texloc[0]);
        EmitVertex();
        gl_Position = vec4(0.0, 0.0, 0.0, 0.0);
        texcoord = vec4(0,0,texloc[0]);
        EmitVertex();
        EndPrimitive();
    }
    '''
    frag_entity = '''
    #version 330
    out vec4 FragColor;
    uniform sampler2D atlas;
    in vec2 texcoord;
    uniform vec4 night;
    vec2 hash22(vec2 p)
    {
        p = p*mat2(127.1,311.7,269.5,183.3);
    	p = -1.0 + 2.0 * fract(sin(p)*43758.5453123);
    	return sin(p*6.283);
    }
    void main() {
        vec4 colour = texture(atlas, texcoord) * night;
        if (colour.w > 0)
        colour += (hash22(texcoord) / 50).x;
        FragColor = colour;
    }
    '''