#------------------------------- func -------------------------------
#-------------------------------
#may be can make a source viewer, others source cover with mask, select source will be high-lighted...

class ExceptionPexpect(Exception):

    """Base class for all exceptions raised by this module.
    """

    def __init__(self, value):

        self.value = value

    def __str__(self):

        return str(self.value)

    def get_trace(self):

        """This returns an abbreviated stack trace with lines that only concern
        the caller. In other words, the stack trace inside the Pexpect module
        is not included. """

        tblist = traceback.extract_tb(sys.exc_info()[2])
        #tblist = filter(self.__filter_not_pexpect, tblist)
        tblist = [item for item in tblist if self.__filter_not_pexpect(item)]
        tblist = traceback.format_list(tblist)
        return ''.join(tblist)

    def __filter_not_pexpect(self, trace_list_item):

        """This returns True if list item 0 the string 'pexpect.py' in it. """

        if trace_list_item[0].find('pexpect.py') == -1:
            return True
        else:
            return False

class EOF(ExceptionPexpect):

    """Raised when EOF is read from a child. This usually means the child has exited."""

class TIMEOUT(ExceptionPexpect):

    """Raised when a read time exceeds the timeout. """

#------------------------------- run -------------------------------
#types.StringTypes - (<type 'str'>, <type 'unicode'>)
    child_result_list = []
            if type(child.after) in types.StringTypes:
                child_result_list.append(child.before + child.after)
#use except as a return value
        except TIMEOUT, e:
            child_result_list.append(child.before)
            break
        except EOF, e:
#[].append
            child_result_list.append(child.before)
            break
#''.join([])
    child_result = ''.join(child_result_list)
#-------------------------------
#responses is a events 
            if type(responses[index]) in types.StringTypes:
                child.send(responses[index])
            elif type(responses[index]) is types.FunctionType:
#locals() - update and return a dictionary representing the current local symbol table
                callback_result = responses[index](locals())
#any callback is function that takes a dictionary which contains all the locals from the run() function 
#so you can access the child spawn object or any other variable defined in run()
                sys.stdout.flush()
                if type(callback_result) in types.StringTypes:
                    child.send(callback_result)
                elif callback_result:
                    break
            else:
#TypeError
                raise TypeError ('The callback must be a string or function type.')
#------------------------------- spawn -------------------------------
#use __str__ to describe the object info
    def __str__(self):
        """This returns a human-readable string that represents the state of
        the object. """

        s = []
        s.append(repr(self))
        s.append('version: ' + __version__ + ' (' + __revision__ + ')')
        s.append('command: ' + str(self.command))
        s.append('args: ' + str(self.args))
        s.append('searcher: ' + str(self.searcher))
        s.append('buffer (last 100 chars): ' + str(self.buffer)[-100:])
        s.append('before (last 100 chars): ' + str(self.before)[-100:])
        s.append('after: ' + str(self.after))
        s.append('match: ' + str(self.match))
        s.append('match_index: ' + str(self.match_index))
        s.append('exitstatus: ' + str(self.exitstatus))
        s.append('flag_eof: ' + str(self.flag_eof))
        s.append('pid: ' + str(self.pid))
        s.append('child_fd: ' + str(self.child_fd))
        s.append('closed: ' + str(self.closed))
        s.append('timeout: ' + str(self.timeout))
        s.append('delimiter: ' + str(self.delimiter))
        s.append('logfile: ' + str(self.logfile))
        s.append('logfile_read: ' + str(self.logfile_read))
        s.append('logfile_send: ' + str(self.logfile_send))
        s.append('maxread: ' + str(self.maxread))
        s.append('ignorecase: ' + str(self.ignorecase))
        s.append('searchwindowsize: ' + str(self.searchwindowsize))
        s.append('delaybeforesend: ' + str(self.delaybeforesend))
        s.append('delayafterclose: ' + str(self.delayafterclose))
        s.append('delayafterterminate: ' + str(self.delayafterterminate))
        return '\n'.join(s)
#-------------------------------
#check type
        if type (args) != type([]):
            raise TypeError ('The argument, args, must be a list.')

#-------------------------------
#assert
        assert self.pid is None, 'The pid member should be None.'
        assert self.command is not None, 'The command member should not be None.'

#-------------------------------
#resource, signal, os, selece, ... 
            max_fd = resource.getrlimit(resource.RLIMIT_NOFILE)[0]

            signal.signal(signal.SIGHUP, signal.SIG_IGN)

            if self.cwd is not None:
                os.chdir(self.cwd)
            if self.env is None:
                os.execv(self.command, self.args)
            else:
                os.execvpe(self.command, self.args, self.env)

#-------------------------------
#file ops...
            if self.logfile is not None:
                self.logfile.write (s)
                self.logfile.flush()

#------------------------------- expect -------------------------------
#use except as a normal branch
        except EOF, e:
            self.buffer = ''
            self.before = incoming
            self.after = EOF
            index = searcher.eof_index
            if index >= 0:
                self.match = EOF
                self.match_index = index
                return self.match_index
            else:
                self.match = None
                self.match_index = None
                raise EOF (str(e) + '\n' + str(self))
        except TIMEOUT, e:
            self.buffer = incoming
            self.before = incoming
            self.after = TIMEOUT
            index = searcher.timeout_index
            if index >= 0:
                self.match = TIMEOUT
                self.match_index = index
                return self.match_index
            else:
                self.match = None
                self.match_index = None
                raise TIMEOUT (str(e) + '\n' + str(self))
        except:
            self.before = incoming
            self.after = None
            self.match = None
            self.match_index = None
            raise


















#------------------------------- which -------------------------------
def which (filename):

    """This takes a given filename; tries to find it in the environment path;
    then checks if it is executable. This returns the full path to the filename
    if found and executable. Otherwise this returns None."""

    # Special case where filename already contains a path.
    if os.path.dirname(filename) != '':
        if os.access (filename, os.X_OK):
            return filename

    if not os.environ.has_key('PATH') or os.environ['PATH'] == '':
        p = os.defpath
    else:
        p = os.environ['PATH']

    # Oddly enough this was the one line that made Pexpect
    # incompatible with Python 1.5.2.
    #pathlist = p.split (os.pathsep)
    pathlist = string.split (p, os.pathsep)

    for path in pathlist:
        f = os.path.join(path, filename)
        if os.access(f, os.X_OK):
            return f
    return None

#------------------------------- sendcontrol, sendeof, sendintr -------------------------------
    def sendcontrol(self, char):

        """This sends a control character to the child such as Ctrl-C or
        Ctrl-D. For example, to send a Ctrl-G (ASCII 7)::

            child.sendcontrol('g')

        See also, sendintr() and sendeof().
        """

        char = char.lower()
        a = ord(char)
        if a>=97 and a<=122:
            a = a - ord('a') + 1
            return self.send (chr(a))
        d = {'@':0, '`':0,
            '[':27, '{':27,
            '\\':28, '|':28,
            ']':29, '}': 29,
            '^':30, '~':30,
            '_':31,
            '?':127}
        if char not in d:
            return 0
        return self.send (chr(d[char]))

#-------------------------------
#termios
    def sendeof(self):

        """This sends an EOF to the child. This sends a character which causes
        the pending parent output buffer to be sent to the waiting child
        program without waiting for end-of-line. If it is the first character
        of the line, the read() in the user program returns 0, which signifies
        end-of-file. This means to work as expected a sendeof() has to be
        called at the beginning of a line. This method does not send a newline.
        It is the responsibility of the caller to ensure the eof is sent at the
        beginning of a line. """

        ### Hmmm... how do I send an EOF?
        ###C  if ((m = write(pty, *buf, p - *buf)) < 0)
        ###C      return (errno == EWOULDBLOCK) ? n : -1;
        #fd = sys.stdin.fileno()
        #old = termios.tcgetattr(fd) # remember current state
        #attr = termios.tcgetattr(fd)
        #attr[3] = attr[3] | termios.ICANON # ICANON must be set to recognize EOF
        #try: # use try/finally to ensure state gets restored
        #    termios.tcsetattr(fd, termios.TCSADRAIN, attr)
        #    if hasattr(termios, 'CEOF'):
        #        os.write (self.child_fd, '%c' % termios.CEOF)
        #    else:
        #        # Silly platform does not define CEOF so assume CTRL-D
        #        os.write (self.child_fd, '%c' % 4)
        #finally: # restore state
        #    termios.tcsetattr(fd, termios.TCSADRAIN, old)
        if hasattr(termios, 'VEOF'):
            char = termios.tcgetattr(self.child_fd)[6][termios.VEOF]
        else:
            # platform does not define VEOF so assume CTRL-D
            char = chr(4)
        self.send(char)

#-------------------------------
    def sendintr(self):

        """This sends a SIGINT to the child. It does not require
        the SIGINT to be the first character on a line. """

        if hasattr(termios, 'VINTR'):
            char = termios.tcgetattr(self.child_fd)[6][termios.VINTR]
        else:
            # platform does not define VINTR so assume CTRL-C
            char = chr(3)
        self.send (char)

#------------------------------- terminate, wait, isalive -------------------------------
    def terminate(self, force=False):

        """This forces a child process to terminate. It starts nicely with
        SIGHUP and SIGINT. If "force" is True then moves onto SIGKILL. This
        returns True if the child was terminated. This returns False if the
        child could not be terminated. """

        if not self.isalive():
            return True
        try:
            self.kill(signal.SIGHUP)
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            self.kill(signal.SIGCONT)
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            self.kill(signal.SIGINT)
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            if force:
                self.kill(signal.SIGKILL)
                time.sleep(self.delayafterterminate)
                if not self.isalive():
                    return True
                else:
                    return False
            return False
        except OSError, e:
            # I think there are kernel timing issues that sometimes cause
            # this to happen. I think isalive() reports True, but the
            # process is dead to the kernel.
            # Make one last attempt to see if the kernel is up to date.
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            else:
                return False

#-------------------------------
    def wait(self):

        """This waits until the child exits. This is a blocking call. This will
        not read any data from the child, so this will block forever if the
        child has unread output and has terminated. In other words, the child
        may have printed output then called exit(); but, technically, the child
        is still alive until its output is read. """

        if self.isalive():
            pid, status = os.waitpid(self.pid, 0)
        else:
            raise ExceptionPexpect ('Cannot wait for dead child process.')
        self.exitstatus = os.WEXITSTATUS(status)
        if os.WIFEXITED (status):
            self.status = status
            self.exitstatus = os.WEXITSTATUS(status)
            self.signalstatus = None
            self.terminated = True
        elif os.WIFSIGNALED (status):
            self.status = status
            self.exitstatus = None
            self.signalstatus = os.WTERMSIG(status)
            self.terminated = True
        elif os.WIFSTOPPED (status):
            raise ExceptionPexpect ('Wait was called for a child process that is stopped. This is not supported. Is some other process attempting job control with our child pid?')
        return self.exitstatus

#-------------------------------
    def isalive(self):

        """This tests if the child process is running or not. This is
        non-blocking. If the child was terminated then this will read the
        exitstatus or signalstatus of the child. This returns True if the child
        process appears to be running or False if not. It can take literally
        SECONDS for Solaris to return the right status. """

        if self.terminated:
            return False

        if self.flag_eof:
            # This is for Linux, which requires the blocking form of waitpid to get
            # status of a defunct process. This is super-lame. The flag_eof would have
            # been set in read_nonblocking(), so this should be safe.
            waitpid_options = 0
        else:
            waitpid_options = os.WNOHANG

        try:
            pid, status = os.waitpid(self.pid, waitpid_options)
        except OSError, e: # No child processes
            if e[0] == errno.ECHILD:
                raise ExceptionPexpect ('isalive() encountered condition where "terminated" is 0, but there was no child process. Did someone else call waitpid() on our process?')
            else:
                raise e

        # I have to do this twice for Solaris. I can't even believe that I figured this out...
        # If waitpid() returns 0 it means that no child process wishes to
        # report, and the value of status is undefined.
        if pid == 0:
            try:
                pid, status = os.waitpid(self.pid, waitpid_options) ### os.WNOHANG) # Solaris!
            except OSError, e: # This should never happen...
                if e[0] == errno.ECHILD:
                    raise ExceptionPexpect ('isalive() encountered condition that should never happen. There was no child process. Did someone else call waitpid() on our process?')
                else:
                    raise e

            # If pid is still 0 after two calls to waitpid() then
            # the process really is alive. This seems to work on all platforms, except
            # for Irix which seems to require a blocking call on waitpid or select, so I let read_nonblocking
            # take care of this situation (unfortunately, this requires waiting through the timeout).
            if pid == 0:
                return True

        if pid == 0:
            return True

        if os.WIFEXITED (status):
            self.status = status
            self.exitstatus = os.WEXITSTATUS(status)
            self.signalstatus = None
            self.terminated = True
        elif os.WIFSIGNALED (status):
            self.status = status
            self.exitstatus = None
            self.signalstatus = os.WTERMSIG(status)
            self.terminated = True
        elif os.WIFSTOPPED (status):
            raise ExceptionPexpect ('isalive() encountered condition where child process is stopped. This is not supported. Is some other process attempting job control with our child pid?')
        return False

























