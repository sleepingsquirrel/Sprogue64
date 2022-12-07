

class shader_storage:
    vert_wall = '''
    #version 330
    in vec2 apos;
    void main()
    {
        gl_Position = vec4(apos, 0.1, 1);
        
    }
    '''
    frag_wall = '''
    
    #version 330
    out vec4 FragColor;
    
     

    void main()
    {
        FragColor = vertexColor;
    } 
    
    '''