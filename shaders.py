

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
        //FragColor = vec4(texture(atlas, tex));
        vec4 dat = texture(atlas, tex);
        if (dat.r / 2 > (abs(tex.y - 0.5))) {
            FragColor = vec4(0.5,0.5,0.5,1.0);
        }
        else {
            if (tex.y < 0.5){
                FragColor = vec4(1.0,1.0,1.0,1.0);
            }
            else{
                vec2 rand = hash22(vec2(round((tex.x+rot)*w)/w,round((tex.y)*h)/h));
                vec3 col = vec3(0);
                if (rand.x > 0.99){
                    col = vec3(rand.y);
                }
                FragColor = vec4(vec3(col),1.0);
            }
           
        }
    } 
    
    '''