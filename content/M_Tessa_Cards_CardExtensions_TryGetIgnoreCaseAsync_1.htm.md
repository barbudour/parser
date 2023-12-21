#
CardExtensions.TryGetIgnoreCaseAsync(StringDictionaryStorage<CardSectionPermissionInfo>,
String, ICardMetadata, CancellationToken) - метод
Возвращает разрешения для секции карточки, полученной без учёта регистра, или
null, если такая секция отсутствует.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<CardSectionPermissionInfo> TryGetIgnoreCaseAsync(
    	this StringDictionaryStorage<CardSectionPermissionInfo> sections,
    	string sectionName,
    	ICardMetadata cardMetadata = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetIgnoreCaseAsync ( 
    	sections As StringDictionaryStorage(Of CardSectionPermissionInfo),
    	sectionName As String,
    	Optional cardMetadata As ICardMetadata = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardSectionPermissionInfo)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ValueTask<CardSectionPermissionInfo^> TryGetIgnoreCaseAsync(
    	StringDictionaryStorage<CardSectionPermissionInfo^>^ sections, 
    	String^ sectionName, 
    	ICardMetadata^ cardMetadata = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetIgnoreCaseAsync : 
            sections : StringDictionaryStorage<CardSectionPermissionInfo> * 
            sectionName : string * 
            ?cardMetadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cardMetadata = defaultArg cardMetadata null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardSectionPermissionInfo> 
#### Параметры
sections
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardSectionPermissionInfo](T_Tessa_Cards_CardSectionPermissionInfo.htm)>
    Коллекция разрешений для секций в объекте карточки.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции без учёта регистра.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm) (Optional)
     Метаинформация по типу карточки или общая метаинформация, которые используются для корректировки регистра в имени секции. Также можно указать null, если корректировка регистра будет возможна только по данным, содержащимся в объекте карточки. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardSectionPermissionInfo](T_Tessa_Cards_CardSectionPermissionInfo.htm)>  
Секция карточки, полученная без учёта регистра, или null, если такая секция
отсутствует.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardSectionPermissionInfo](T_Tessa_Cards_CardSectionPermissionInfo.htm)>.
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[TryGetIgnoreCaseAsync -
перегрузка](Overload_Tessa_Cards_CardExtensions_TryGetIgnoreCaseAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
