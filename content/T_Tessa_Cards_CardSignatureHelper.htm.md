# CardSignatureHelper - класс
Хэлперы и константы для взаимодействия с подписями файлов, расположенных в
карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardSignatureHelper
VB __Копировать
     Public NotInheritable Class CardSignatureHelper
C++ __Копировать
     public ref class CardSignatureHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardSignatureHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardSignatureHelper
##  __Методы
[AnySignatureRow(Card, Func<CardFile, CardRow,
Boolean>)](M_Tessa_Cards_CardSignatureHelper_AnySignatureRow.htm)|  Возвращает
признак того, что среди всех подписей всех файлов хотя бы одна строка
удовлетворяет заданному условию signaturePredicateFunc.  
---|---  
[AnySignatureRow(CardFile, Func<CardFile, CardRow,
Boolean>)](M_Tessa_Cards_CardSignatureHelper_AnySignatureRow_1.htm)|
Возвращает признак того, что среди всех подписей заданного файла хотя бы одна
строка удовлетворяет заданному условию signaturePredicateFunc.  
[ForEachSignatureRow(Card, Action<CardFile,
CardRow>)](M_Tessa_Cards_CardSignatureHelper_ForEachSignatureRow.htm)|
Выполняет заданный делегат для каждой строки с подписью каждого файла в
заданной карточке. Возвращает признак того, что делегат был выполнен хотя бы
один раз, т.е. была найдена хотя бы одна подпись в одном из файлов.  
[ForEachSignatureRow(CardFile, Action<CardFile,
CardRow>)](M_Tessa_Cards_CardSignatureHelper_ForEachSignatureRow_1.htm)|
Выполняет заданный делегат для каждой строки с подписью в заданном файле.
Возвращает признак того, что делегат был выполнен хотя бы один раз, т.е. в
файле была найдена хотя бы одна подпись.  
[GetLinkedToLastVersion](M_Tessa_Cards_CardSignatureHelper_GetLinkedToLastVersion.htm)|
Возвращает признак того, что строка с ЭЦП связана с последней версией файла,
поэтому ссылка на идентификатор версии будет обновлена при сохранении на
случай, если для файла новая версия будет создана позже, чем была добавлена
подпись. Если признак не был установлен, то возвращается false.  
[RemoveLinkedToLastVersion](M_Tessa_Cards_CardSignatureHelper_RemoveLinkedToLastVersion.htm)|
Удаляет признак того, что строка с ЭЦП связана с последней версией файла.  
[SetLinkedToLastVersion](M_Tessa_Cards_CardSignatureHelper_SetLinkedToLastVersion.htm)|
Устанавливает признак того, что строка с ЭЦП связана с последней версией
файла, поэтому ссылка на идентификатор версии будет обновлена при сохранении
на случай, если для файла новая версия будет создана позже, чем была добавлена
подпись.  
## __Поля
[CommentFieldID](F_Tessa_Cards_CardSignatureHelper_CommentFieldID.htm)|
Идентификатор поля с комментарием к подписи, который может использоваться для
указания источника подписи и прочих вещей.  
---|---  
[CompanyFieldID](F_Tessa_Cards_CardSignatureHelper_CompanyFieldID.htm)|
Идентификатор поля с названием организации, которое указано в файле подписи.  
[DataFieldID](F_Tessa_Cards_CardSignatureHelper_DataFieldID.htm)|
Идентификатор поля с бинарными данными файла подписи. По умолчанию такое поле
не загружается при открытии карточки.  
[EventFieldID](F_Tessa_Cards_CardSignatureHelper_EventFieldID.htm)|
Идентификатор поля с событием, в результате которого была добавлена версия.  
[IssuerNameFieldID](F_Tessa_Cards_CardSignatureHelper_IssuerNameFieldID.htm)|
Идентификатор поля с именем подписанта, которое указано в файле подписи.  
[SectionID](F_Tessa_Cards_CardSignatureHelper_SectionID.htm)|  Идентификатор
секции с подписями файлов.  
[SectionName](F_Tessa_Cards_CardSignatureHelper_SectionName.htm)|  Название
секции с подписями файлов.  
[SerialNumberFieldID](F_Tessa_Cards_CardSignatureHelper_SerialNumberFieldID.htm)|
Серийный номер сертификата, который указан в файле подписи.  
[SignatureProfileFieldID](F_Tessa_Cards_CardSignatureHelper_SignatureProfileFieldID.htm)|
Идентификатор поля с профилем подписи  
[SignatureTypeFieldID](F_Tessa_Cards_CardSignatureHelper_SignatureTypeFieldID.htm)|
Идентификатор поля с типом подписи  
[SignedFieldID](F_Tessa_Cards_CardSignatureHelper_SignedFieldID.htm)|
Идентификатор поля с датой подписания, которая указана в файле подписи.  
[SubjectNameFieldID](F_Tessa_Cards_CardSignatureHelper_SubjectNameFieldID.htm)|
Идентификатор поля с ФИО сотрудника, которое указано в файле подписи.  
[UserFieldID](F_Tessa_Cards_CardSignatureHelper_UserFieldID.htm)|
Идентификатор поля со ссылкой на пользователя, который добавил версию.  
[VersionFieldID](F_Tessa_Cards_CardSignatureHelper_VersionFieldID.htm)|
Идентификатор поля с версией файла.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
