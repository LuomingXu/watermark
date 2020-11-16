Add Watermark
=
    Write for id card
    Python(3.8)
    

#### Args
    details in code
    
    
#### former
![image](image.png)


#### after
![image](after.png)

#### Dependency
+ Pillow

#### License
[Apache-2.0 License](LICENSE)

#### Tip
```python
    # add different background color
    image: Image = PIL.Image.open("background_less.png")
    background: Image = PIL.Image.new("RGBA", image.size, (255, 0, 0))
    background.paste(image, (0, 0, image.width, image.height), image)
    background.save("test.png")
```