

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
    uniform sampler2D atlas;
    void main()
    {
        //FragColor = vec4(texture(atlas, tex));
        vec4 dat = texture(atlas, tex);
        if (dat.r / 2 > (abs(tex.y - 0.5))) {
            FragColor = vec4(0.5,0.5,0.5,1.0);
        }
        else {
            FragColor = vec4(1.0,1.0,1.0,1.0);
        }
    } 
    
    '''