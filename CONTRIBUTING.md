# Contributing Guide

Thanks for your interest in contributing! This guide will help you get started.

## How to Contribute

### 1. Types of Contributions We Welcome

- **Bug fixes** - Fix issues or improve stability
- **New features** - Add new detection types (smiles, winks, etc.)
- **Documentation** - Improve guides, add examples, fix typos
- **UI/UX improvements** - Better visual feedback, cleaner interface
- **Performance optimizations** - Speed improvements, resource efficiency
- **Testing** - Add tests, improve reliability
- **Platform support** - Improve Windows/macOS/Linux compatibility

### 2. Getting Started

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/simple-mediapipe-project.git
   cd simple-mediapipe-project
   ```
   
   Or clone the original repository:
   ```bash
   git clone https://github.com/aaronhubhachen/simple-mediapipe-project.git
   cd simple-mediapipe-project
   ```

3. **Set up development environment**
   
   **Windows:**
   ```bash
   python3.11 -m pip install -r requirements.txt
   ```
   
   **macOS/Linux:**
   ```bash
   python3.11 -m pip install -r requirements.txt
   chmod +x run.sh
   ```

4. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

### 3. Making Changes

#### Code Style Guidelines

- **Python:** Follow PEP 8 style guide
- **Comments:** Write clear, helpful comments
- **Documentation:** Update README/docs if you change functionality
- **Commit messages:** Be descriptive

Good commit messages:
```bash
git commit -m "Add smile detection feature"
git commit -m "Fix webcam initialization on Linux"
git commit -m "Update macOS setup instructions"
```

Bad commit messages:
```bash
git commit -m "fix"
git commit -m "update"
git commit -m "changes"
```

#### Code Organization

- Keep functions small and focused
- Add docstrings to new functions
- Use meaningful variable names
- Follow existing code structure

Example of good code:
```python
def detect_smile(face_landmarks):
    """
    Detect if the person is smiling.
    
    Args:
        face_landmarks: MediaPipe face landmarks object
        
    Returns:
        bool: True if smiling, False otherwise
    """
    left_mouth = face_landmarks.landmark[61]
    right_mouth = face_landmarks.landmark[291]
    
    # Calculate smile based on mouth corners
    smile_threshold = 0.02
    return (left_mouth.y < right_mouth.y - smile_threshold)
```

### 4. Testing Your Changes

Before submitting:

1. Test on your platform
   ```bash
   python3.11 main.py
   ```

2. Check for errors
   - No Python errors/exceptions
   - Webcam works properly
   - Detection functions as expected

3. Test edge cases
   - No face in frame
   - Multiple faces (if applicable)
   - Poor lighting conditions
   - Different camera angles

4. Cross-platform testing (if possible)
   - Windows
   - macOS
   - Linux

### 5. Submitting Changes

1. Commit your changes
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   ```

2. Push to your fork
   ```bash
   git push origin feature/your-feature-name
   ```

3. Create a Pull Request
   - Go to GitHub
   - Click "New Pull Request"
   - Select your branch
   - Write a clear description of your changes
   - Reference any related issues

### 6. Pull Request Guidelines

Your PR should include:

- Clear description of what changed
- Why the change was needed
- How to test the change
- Screenshots/videos (if UI changes)
- Updated documentation (if needed)
- No breaking changes (or clearly noted)

PR Description Template:
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
How to test these changes:
1. Step one
2. Step two
3. Expected result

## Platform Tested
- [ ] Windows
- [ ] macOS
- [ ] Linux

## Screenshots
(if applicable)
```

## Feature Ideas

Want to contribute but don't know where to start? Try these:

### Beginner-Friendly
- Add different color themes
- Improve error messages
- Add keyboard shortcuts
- Create example images
- Fix typos in documentation

### Intermediate
- Add smile detection
- Add wink detection
- Add multiple image support (3+ states)
- Add sound effects
- Add recording feature
- Improve detection algorithm

### Advanced
- Multi-face tracking
- Hand gesture detection (MediaPipe Hands)
- Background replacement
- Face filters/effects
- Real-time performance monitoring
- GPU acceleration support

## Code Review Process

1. Maintainer reviews your PR
2. Feedback may be requested
3. Make changes if needed
4. Approval and merge

## Reporting Bugs

Found a bug? Please open an issue with:

1. **Clear title** - Describe the bug briefly
2. **Environment**
   - OS and version
   - Python version
   - Package versions
3. **Steps to reproduce**
   - What you did
   - What happened
   - What should have happened
4. **Screenshots/videos** if applicable
5. **Error messages** (full traceback)

Bug Report Template:
```markdown
## Bug Description
Clear description of the bug

## Environment
- OS: macOS 14.1
- Python: 3.11.5
- MediaPipe: 0.10.14
- OpenCV: 4.11.0.86

## Steps to Reproduce
1. Start the application
2. Do X
3. See error

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Error Messages
```
Paste error here
```

## Additional Context
Any other relevant information
```

## Documentation Contributions

Improving documentation is a great way to contribute!

Areas needing help:
- Fixing typos and grammar
- Adding more examples
- Creating video tutorials
- Translating to other languages
- Platform-specific guides
- FAQ section

How to contribute docs:
1. Edit the `.md` file
2. Preview your changes
3. Submit PR with clear description

## Community Guidelines

- Be respectful and inclusive
- Help others learn
- Give constructive feedback
- Celebrate successes
- Have fun

## Questions?

- Check existing issues and PRs
- Read the documentation
- Ask in your PR or issue
- Be patient - we're volunteers!

## Recognition

All contributors will be:
- Added to contributors list
- Credited in release notes
- Appreciated!

Thank you for contributing!

---

Ready to contribute?
1. Fork the repo
2. Make your changes
3. Submit a PR

