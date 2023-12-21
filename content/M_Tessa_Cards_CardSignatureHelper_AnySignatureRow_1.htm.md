# CardSignatureHelper.AnySignatureRow(CardFile, Func<CardFile, CardRow,
Boolean>) - метод
Возвращает признак того, что среди всех подписей заданного файла хотя бы одна
строка удовлетворяет заданному условию signaturePredicateFunc.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool AnySignatureRow(
    	CardFile file,
    	Func<CardFile, CardRow, bool> signaturePredicateFunc
    )
VB __Копировать
     Public Shared Function AnySignatureRow ( 
    	file As CardFile,
    	signaturePredicateFunc As Func(Of CardFile, CardRow, Boolean)
    ) As Boolean
C++ __Копировать
     public:
    static bool AnySignatureRow(
    	CardFile^ file, 
    	Func<CardFile^, CardRow^, bool>^ signaturePredicateFunc
    )
F# __Копировать
     static member AnySignatureRow : 
            file : CardFile * 
            signaturePredicateFunc : Func<CardFile, CardRow, bool> -> bool 
#### Параметры
file [CardFile](T_Tessa_Cards_CardFile.htm)
    Файл, в которой расположены подписи.
signaturePredicateFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[CardFile](T_Tessa_Cards_CardFile.htm),
[CardRow](T_Tessa_Cards_CardRow.htm),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Предикат, выполняемый для всех подписей заданного файла. Первым параметром получает файл с подписью file, а вторым - строку подписи. Если предикат возвращает true, то обход подписей прекращается и метод возвращает true. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что среди всех подписей заданного файла хотя бы одна строка
удовлетворяет заданному условию signaturePredicateFunc.
## __См. также
#### Ссылки
[CardSignatureHelper - ](T_Tessa_Cards_CardSignatureHelper.htm)
[AnySignatureRow -
перегрузка](Overload_Tessa_Cards_CardSignatureHelper_AnySignatureRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
