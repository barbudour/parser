# FileConverterExtensions.GetOutputStreamOrThrow - метод
Возвращает поток на выходной файл или выбрасывает исключение, если файл не
найден или произошла другая ошибка при его открытии. Возвращённый поток
необходимо закрыть вызовом
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose).
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Stream GetOutputStreamOrThrow(
    	this IFileConverterContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetOutputStreamOrThrow ( 
    	context As IFileConverterContext
    ) As Stream
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Stream^ GetOutputStreamOrThrow(
    	IFileConverterContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetOutputStreamOrThrow : 
            context : IFileConverterContext -> Stream 
#### Параметры
context
[IFileConverterContext](T_Tessa_FileConverters_IFileConverterContext.htm)
    Контекст операции конвертации.
#### Возвращаемое значение
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)  
Поток на выходной файл.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IFileConverterContext](T_Tessa_FileConverters_IFileConverterContext.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[FileConverterExtensions -
](T_Tessa_FileConverters_FileConverterExtensions.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
