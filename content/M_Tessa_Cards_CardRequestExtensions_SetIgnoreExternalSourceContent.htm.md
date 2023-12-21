# CardRequestExtensions.SetIgnoreExternalSourceContent - метод
Устанавливает признак того, что при обработке файла системой не следует
учитывать свойство [ExternalSource](P_Tessa_Cards_CardFile_ExternalSource.htm)
как необходимость копировать контент файла. Например, при создании шаблона
контент копируется средствами расширения и не должен копироваться системой.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetIgnoreExternalSourceContent(
    	this CardFile file,
    	bool ignoreExternalSourceContent = true
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetIgnoreExternalSourceContent ( 
    	file As CardFile,
    	Optional ignoreExternalSourceContent As Boolean = true
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetIgnoreExternalSourceContent(
    	CardFile^ file, 
    	bool ignoreExternalSourceContent = true
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetIgnoreExternalSourceContent : 
            file : CardFile * 
            ?ignoreExternalSourceContent : bool 
    (* Defaults:
            let _ignoreExternalSourceContent = defaultArg ignoreExternalSourceContent true
    *)
    -> unit 
#### Параметры
file [CardFile](T_Tessa_Cards_CardFile.htm)
    Сохраняемый файл.
ignoreExternalSourceContent
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что при обработке файла системой не следует учитывать свойство [ExternalSource](P_Tessa_Cards_CardFile_ExternalSource.htm). 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardFile](T_Tessa_Cards_CardFile.htm). При вызове метода для
экземпляра следует опускать первый параметр. Дополнительные сведения см. в
разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
