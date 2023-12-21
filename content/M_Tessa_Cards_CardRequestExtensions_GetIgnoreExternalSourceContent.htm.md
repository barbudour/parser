# CardRequestExtensions.GetIgnoreExternalSourceContent - метод
Возвращает признак того, что при сохранении карточки могут быть не указаны
токены безопасности, поэтому не следует показывать соответствующее
предупреждение. Если признак не был установлен, то возвращается false.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool GetIgnoreExternalSourceContent(
    	this CardFile file
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetIgnoreExternalSourceContent ( 
    	file As CardFile
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool GetIgnoreExternalSourceContent(
    	CardFile^ file
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetIgnoreExternalSourceContent : 
            file : CardFile -> bool 
#### Параметры
file [CardFile](T_Tessa_Cards_CardFile.htm)
    Сохраняемый файл.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что при обработке файла системой не следует учитывать свойство
[ExternalSource](P_Tessa_Cards_CardFile_ExternalSource.htm). Если признак не
был установлен, то возвращается false.
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
