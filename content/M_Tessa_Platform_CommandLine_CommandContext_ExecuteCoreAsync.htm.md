# CommandContext.ExecuteCoreAsync - метод
When overridden in a derived class, provides execution logic.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override Task ExecuteCoreAsync(
    	TextReader input,
    	TextWriter output,
    	TextWriter error,
    	ArgumentEnumerator args
    )
VB __Копировать
     Protected Overrides Function ExecuteCoreAsync ( 
    	input As TextReader,
    	output As TextWriter,
    	error As TextWriter,
    	args As ArgumentEnumerator
    ) As Task
C++ __Копировать
     protected:
    virtual Task^ ExecuteCoreAsync(
    	TextReader^ input, 
    	TextWriter^ output, 
    	TextWriter^ error, 
    	ArgumentEnumerator^ args
    ) override
F# __Копировать
     abstract ExecuteCoreAsync : 
            input : TextReader * 
            output : TextWriter * 
            error : TextWriter * 
            args : ArgumentEnumerator -> Task 
    override ExecuteCoreAsync : 
            input : TextReader * 
            output : TextWriter * 
            error : TextWriter * 
            args : ArgumentEnumerator -> Task 
#### Параметры
input
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader)
    The [TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader) that represents an input stream.
output
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter)
    The [TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter) that represents an output stream.
error
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter)
    The [TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter) that represents an error stream.
args [ArgumentEnumerator](T_Tessa_Platform_CommandLine_ArgumentEnumerator.htm)
    Command-line arguments which were passed to the command.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __См. также
#### Ссылки
[CommandContext - ](T_Tessa_Platform_CommandLine_CommandContext.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
