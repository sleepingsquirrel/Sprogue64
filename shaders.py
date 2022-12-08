

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
    out vec4 FragColor;
    in vec2 tex;
    void main()
    {
        FragColor = vec4(tex,1,1);
    } 
    
    '''