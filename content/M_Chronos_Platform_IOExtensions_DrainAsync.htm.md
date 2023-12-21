# IOExtensions.DrainAsync - метод
Выполняет асинхронное чтение всех данных, содержащихся для заданного объекта
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader), но
не использует эти данные, и возвращает асинхронную задачу по окончанию чтения.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask DrainAsync(
    	this TextReader textReader,
    	CancellationToken cancellationToken
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function DrainAsync ( 
    	textReader As TextReader,
    	cancellationToken As CancellationToken
    ) As ValueTask
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ValueTask DrainAsync(
    	TextReader^ textReader, 
    	CancellationToken cancellationToken
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member DrainAsync : 
            textReader : TextReader * 
            cancellationToken : CancellationToken -> ValueTask 
#### Параметры
textReader
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader)
    Объект, выполняющий чтение данных.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[IOExtensions - ](T_Chronos_Platform_IOExtensions.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
