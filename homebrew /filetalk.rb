class Filetalk < Formula
  include Language::Python::Virtualenv

  desc "Simplifies your file searches in command line"
  homepage "https://github.com/VijCodes/filetalk"
  url "https://files.pythonhosted.org/packages/source/f/filetalk/filetalk-0.1.0.tar.gz"  # Example URL, replace with actual
  sha256 "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"  # Example SHA-256, replace with actual

  depends_on "python@3.9"

  def install
    virtualenv_install_with_resources
  end
end