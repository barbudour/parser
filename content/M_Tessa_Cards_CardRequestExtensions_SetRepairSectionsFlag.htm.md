# CardRequestExtensions.SetRepairSectionsFlag - метод
Устанавливает флаг, который указывает на то, что нужно починить (добавить)
строковые секции карточки в случае, если они отсутствуют в БД.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetRepairSectionsFlag(
    	this CardStoreRequest request,
    	bool flag
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetRepairSectionsFlag ( 
    	request As CardStoreRequest,
    	flag As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetRepairSectionsFlag(
    	CardStoreRequest^ request, 
    	bool flag
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetRepairSectionsFlag : 
            request : CardStoreRequest * 
            flag : bool -> unit 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
flag [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
