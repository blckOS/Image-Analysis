def load_images():
	image_dose_dict = {}
	image_files = sorted(os.listdir("images"))  # get a list of file names
	
	print(image_files)
	
	for fn in image_files:
	    dose = fn[:3]
	    # the last four letters before the file extension represented the channel
	    channel = fn[-8:-4]
	    # the field number is in the fifth letter
	    field = fn[4]
	    
	    print (fn, dose, channel, field)  # check that our parsing system is correct
	    if dose not in image_dose_dict:
	        image_dose_dict[dose] = {} # create an empty dictionary for each dose

		# load the images into our dictionary
		for fn in image_files:
		    
		    dose = fn[:3]
		    channel = fn[-8:-4]
		    field = fn[4]
		    print (fn, dose, channel, field)
		    
		    A = ndimage.imread("images/" + fn)       # read in the image
		    
		    # original image is an RGB image so we can store the structure to help us 
		    # make RBG images later.
		    original_image_size = A.shape
		    
		    # generate a gray scale image by taking the sum across all three channels            
		    A = numpy.sum(A, axis=2)
		    # scale bar was included in the images.  We can either do some fancy 
		    # work to eliminate the scale bar or we can just crop the images.
		    A = A[:650,:] # cuts off the bottom of the image
		    print (numpy.max(A), numpy.min(A))
		    
		    original_image_size = tuple([650, original_image_size[1], 
		    	                        original_image_size[2]])
		    
		    print(A.shape)
		    
		    if field in image_dose_dict[dose]: pass
		    # if this is a new field, create a new dictionary for it to store the images.
		    else: image_dose_dict[dose][field] = {}
		    # save the image in the appropriate location in our dictionary
		    image_dose_dict[dose][field][channel] = A 

	return image_dose_dict