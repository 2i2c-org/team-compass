(blog:index)=

# Our blog

The [blog at `2i2c.org/blog`](https://2i2c.org/blog) is the primary way that we communicate our work to the external world.

See [](./strategy.md) for how the blog fits into our communications strategy.

## Where is the blog hosted?

Our blog is a subset of our [website repository for 2i2c.org](https://github.com/2i2c-org/2i2c-org.github.io).
See [the blog README](https://github.com/2i2c-org/2i2c-org.github.io/blob/main/content/blog/README.md) for more explanation.

(blog:template)=
## How to submit a blog post idea

All team members are encouraged to submit blog ideas as they do their work.
Do so at this URL:

https://2i2c.org/blog/idea

(blog:write)=
## How to write a blog post

Follow [the blog post guide here](https://github.com/2i2c-org/2i2c-org.github.io/blob/main/content/blog/README.md).

## How to preview your blog post

_Note: you don't actually need to preview the post if it's too much hassle. Just make a PR and the GitHub PR preview can be used to see what it looks like._

To preview your post locally:

- Make sure you've saved the post to disk.
- Ensure that the **date** of the post is before today's date, otherwise the post won't show up (if the post will go up in the future, just temporarily make the date earlier to ensure it shows up)
- [Install Hugo](https://gohugo.io/installation/)
- Run `hugo serve -D` from the repository root

This will run a server that can be used to inspect your post.

## How to edit the blog in the browser without doing anything locally

The easiest way to do all of the above _without ever leaving the browser_ is to do the following:

1. Go to https://github.dev/2i2c-org/2i2c-org.github.io/ this will open a VSCode instance in-browser with the repository loaded up.
    1. Alternatively you can do this from the GitHub UI by going to a repository and pressing `.`
2. Create a new branch that will track your changes by clicking the buttons below and typing in a new branch name: 
    
    ![Image](https://github.com/user-attachments/assets/9566db6d-6105-4b0e-9451-01722fcb2b26)
3. Follow the steps above (you won't be able to preview, don't worry about that).
4. When you're ready to propose a new change, click the "changes" tab, and then the "commit and push" button. 

    ![Image](https://github.com/user-attachments/assets/7cad310d-2620-4ad8-aa99-6e13bb3e4174)
5. Follow the prompts to create a new pull request from within VSCode, or navigate to https://github.com/2i2c-org/2i2c-org.github.io/ and open the PR from there

## How to optimize images

Optimizing images saves space in our repository and in traffic load times.
The [`oxipng` tool](https://github.com/shssoichiro/oxipng) is one that we've used here.
These are brief instructions to get it working based [on the `oxipng` instructions](https://github.com/shssoichiro/oxipng#installing).

It is written in Rust, so you'll need to install `cargo`, install `oxipng`, and then run it.
**To Install Cargo**, follow [the Cargo installation steps](https://doc.rust-lang.org/cargo/getting-started/installation.html).

This will install both Rust and Cargo.

On Windows and Mac, it should be something like:

```
curl https://sh.rustup.rs -sSf | sh
```

One you have done this, you can either run `oxipng` manually or via `pre-commit`.
Both are described below.

### Run `oxipng` with pre-commit

If you have pre-commit installed in this repository, it will run `oxipng` on any `.png` files that have been added automatically.

Simply `cd` into this repository root, then run:

```
$ pip install pre-commit
$ pre-commit install
```

Now when you commit a `.png` file, `oxipng` will be run.

### Run `oxipng` manually

To run `oxipng` manually, follow these steps:

1. **Install `oxipng`**. Use `cargo` to install `oxipng`.

   ```
   cargo install oxipng
   ```
2. **Run the optimization on our images**.
   This one uses several sensible options and will optimize any image in the repository.

   ```
   oxipng -o 4 -i 1 --strip safe --recursive content *.png
   ```

Once the images are optimized, re-commit them to the repository and push the changes.
