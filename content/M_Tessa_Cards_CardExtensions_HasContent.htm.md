# CardExtensions.HasContent - метод
Возвращает признак того, что состояние файла в карточке обязывает предоставить
для такого файла контент, причём карточка с файлом должна сохраняться через
потоковое сохранение.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HasContent(
    	this CardFileState state
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function HasContent ( 
    	state As CardFileState
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool HasContent(
    	CardFileState state
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member HasContent : 
            state : CardFileState -> bool 
#### Параметры
state [CardFileState](T_Tessa_Cards_CardFileState.htm)
     Состояние файла, для которого требуется проверить необходимость наличия контента для соответствующего файла. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если для файла с заданным состоянием в потоке карточки должен
присутствовать контент; false если для файла с заданным состоянием в потоке
карточки должен отсутствовать контент.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardFileState](T_Tessa_Cards_CardFileState.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
