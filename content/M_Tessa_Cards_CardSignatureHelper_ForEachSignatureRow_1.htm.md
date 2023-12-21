# CardSignatureHelper.ForEachSignatureRow(CardFile, Action<CardFile, CardRow>)
- метод
Выполняет заданный делегат для каждой строки с подписью в заданном файле.
Возвращает признак того, что делегат был выполнен хотя бы один раз, т.е. в
файле была найдена хотя бы одна подпись.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ForEachSignatureRow(
    	CardFile file,
    	Action<CardFile, CardRow> signatureAction
    )
VB __Копировать
     Public Shared Function ForEachSignatureRow ( 
    	file As CardFile,
    	signatureAction As Action(Of CardFile, CardRow)
    ) As Boolean
C++ __Копировать
     public:
    static bool ForEachSignatureRow(
    	CardFile^ file, 
    	Action<CardFile^, CardRow^>^ signatureAction
    )
F# __Копировать
     static member ForEachSignatureRow : 
            file : CardFile * 
            signatureAction : Action<CardFile, CardRow> -> bool 
#### Параметры
file [CardFile](T_Tessa_Cards_CardFile.htm)
    Файл, в которой расположены подписи.
signatureAction
[Action](https://learn.microsoft.com/dotnet/api/system.action-2)<[CardFile](T_Tessa_Cards_CardFile.htm),
[CardRow](T_Tessa_Cards_CardRow.htm)>
     Делегат, выполняемый для каждой подписи в заданном файле. Первым параметром получает файл с подписью file, а вторым - строку подписи. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если делегат был выполнен хотя бы один раз; false в противном случае.
## __См. также
#### Ссылки
[CardSignatureHelper - ](T_Tessa_Cards_CardSignatureHelper.htm)
[ForEachSignatureRow -
перегрузка](Overload_Tessa_Cards_CardSignatureHelper_ForEachSignatureRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
