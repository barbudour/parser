# PlatformExtensions.Get<T> \- метод
Возвращает значение из хранилища IDictionary<string, object>, полученное по
ключу key и приведённое к типу T.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static T Get<T>(
    	this IDictionary<string, Object> storage,
    	string key
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function Get(Of T) ( 
    	storage As IDictionary(Of String, Object),
    	key As String
    ) As T
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T>
    static T Get(
    	IDictionary<String^, Object^>^ storage, 
    	String^ key
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member Get : 
            storage : IDictionary<string, Object> * 
            key : string -> 'T 
#### Параметры
storage
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, значение которого требуется получить.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому требуется найти значение.
#### Параметры типа
T
    Тип, к которому требуется привести возвращённое значение.
#### Возвращаемое значение
T  
Значение, полученное по ключу key и приведённое к типу T.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>. При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[PlatformExtensions - ](T_Chronos_Platform_PlatformExtensions.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
