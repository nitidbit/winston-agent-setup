How to write Comments
=====================

Explain one level below the code, then stop. The code says what it does. The comment says
why it is shaped that way. It does not say why that reason is true.

Keep whatever would stop a reader from breaking the code, and cut the rest. Budget about
one line of comment per two or three lines of code. Longer than that and you are narrating
your own investigation rather than helping the next reader.

Too long:

```ruby
# Two runs, because post_cache_spec.rb reloads the whole app and Ruby's Coverage
# discards a file's hits whenever it is re-loaded. A separate run keeps the reload
# away from the other specs, and naming it first keeps it from discarding the rest
# of integration. SimpleCov merges the two runs into one report.
```

Right:

```ruby
# `post_cache_spec.rb` reloads the app which messes up coverage results.  So
# run it separately. SimpleCov then merges the two runs into one report.
```

Three habits that follow from that:

- Plain words beat precise ones when the precision changes no decision. "Messes up" carries everything "discards a file's hits whenever it is re-loaded" was carrying, and reads in half the time.
- Lines of comment should be in proportion to the lines of code, and the importance of the comment. Four lines guarding two shell commands is out of proportion.
- Only defend against the change a reader would actually make. Here that is "why not fold these into one run?" Everything else was me narrating my own investigation.
