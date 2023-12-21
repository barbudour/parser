# CardSignatureHelper.ForEachSignatureRow(Card, Action<CardFile, CardRow>) -
метод
Выполняет заданный делегат для каждой строки с подписью каждого файла в
заданной карточке. Возвращает признак того, что делегат был выполнен хотя бы
один раз, т.е. была найдена хотя бы одна подпись в одном из файлов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ForEachSignatureRow(
    	Card card,
    	Action<CardFile, CardRow> signatureAction
    )
VB __Копировать
     Public Shared Function ForEachSignatureRow ( 
    	card As Card,
    	signatureAction As Action(Of CardFile, CardRow)
    ) As Boolean
C++ __Копировать
     public:
    static bool ForEachSignatureRow(
    	Card^ card, 
    	Action<CardFile^, CardRow^>^ signatureAction
    )
F# __Копировать
     static member ForEachSignatureRow : 
            card : Card * 
            signatureAction : Action<CardFile, CardRow> -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, в которой расположены файлы с подписями.
signatureAction
[Action](https://learn.microsoft.com/dotnet/api/system.action-2)<[CardFile](T_Tessa_Cards_CardFile.htm),
[CardRow](T_Tessa_Cards_CardRow.htm)>
     Делегат, выполняемый для каждой подписи в каждом файле. Первым параметром получает файл с подписью, а вторым - строку подписи. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если делегат был выполнен хотя бы один раз; false в противном случае.
## __См. также
#### Ссылки
[CardSignatureHelper - ](T_Tessa_Cards_CardSignatureHelper.htm)
[ForEachSignatureRow -
перегрузка](Overload_Tessa_Cards_CardSignatureHelper_ForEachSignatureRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
