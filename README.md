## Dumbot-API

### Why was it Created?
It was created as a helper-api for `ppt-dumbot` to access the database items without cluttering up the main codebase.

### Can I run it on my machine?
Yes, it can run locally but you can't access the ✨ main database✨ , you can however create your own database and replace the 
`client: str = os.environ.get("mongoDb")` [here](https://github.com/Rodrous/databaseApi/blob/main/logic_layer/backend.py) to `client: str = your mongodb access key`. 

### How to run locally?
Since its built with `fast-api` you can just run:
 ```
    uvicorn main:app --reload
 ```

## Todo List
- [ ] Add Authentication to limit access to database.
- [X] Add GET methods to retrieve items

## Contributions
Any type of Contribution is Appreciated.
### Code Style
- Use [PEP-8](https://www.python.org/dev/peps/pep-0008/) guidelines.
- Use [typehinting](https://docs.python.org/3/library/typing.html) wherever possible.



## Contributors
Special Thanks to [EvilGraffes](https://github.com/EvilGiraffes) and Blackfinix for all the content in the Database.

## FAQ
➡ Hey, do you think it was a Good Idea to publicize your API without adding a Proper Authentication System?

    No :)




