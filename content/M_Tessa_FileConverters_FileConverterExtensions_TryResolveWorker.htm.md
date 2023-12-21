# FileConverterExtensions.TryResolveWorker - метод
Получает объект
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm) из
контейнера для конвертации файла в формат outputFormat или null, если объект
не зарегистрирован.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IFileConverterWorker TryResolveWorker(
    	this IUnityContainer container,
    	FileConverterFormat outputFormat
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryResolveWorker ( 
    	container As IUnityContainer,
    	outputFormat As FileConverterFormat
    ) As IFileConverterWorker
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IFileConverterWorker^ TryResolveWorker(
    	IUnityContainer^ container, 
    	FileConverterFormat outputFormat
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryResolveWorker : 
            container : IUnityContainer * 
            outputFormat : FileConverterFormat -> IFileConverterWorker 
#### Параметры
container IUnityContainer
    Контейнер, из которого запрашивается объект.
outputFormat
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
    Формат файла, для конвертации в который требуется получить объект.
#### Возвращаемое значение
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm)  
Объект [IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm)
из контейнера для конвертации файла в формат outputFormat или null, если
объект не зарегистрирован.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа IUnityContainer. При вызове метода для экземпляра следует
опускать первый параметр. Дополнительные сведения см. в разделе [Методы
расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[FileConverterExtensions -
](T_Tessa_FileConverters_FileConverterExtensions.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
