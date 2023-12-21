# CardSignatureHelper.AnySignatureRow(Card, Func<CardFile, CardRow, Boolean>)
- метод
Возвращает признак того, что среди всех подписей всех файлов хотя бы одна
строка удовлетворяет заданному условию signaturePredicateFunc.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool AnySignatureRow(
    	Card card,
    	Func<CardFile, CardRow, bool> signaturePredicateFunc
    )
VB __Копировать
     Public Shared Function AnySignatureRow ( 
    	card As Card,
    	signaturePredicateFunc As Func(Of CardFile, CardRow, Boolean)
    ) As Boolean
C++ __Копировать
     public:
    static bool AnySignatureRow(
    	Card^ card, 
    	Func<CardFile^, CardRow^, bool>^ signaturePredicateFunc
    )
F# __Копировать
     static member AnySignatureRow : 
            card : Card * 
            signaturePredicateFunc : Func<CardFile, CardRow, bool> -> bool 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, в которой расположены файлы с подписями.
signaturePredicateFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[CardFile](T_Tessa_Cards_CardFile.htm),
[CardRow](T_Tessa_Cards_CardRow.htm),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
     Предикат, выполняемый для всех подписей всех файлов. Первым параметром получает файл с подписью, а вторым - строку подписи. Если предикат возвращает true, то обход подписей прекращается и метод возвращает true. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что среди всех подписей всех файлов хотя бы одна строка
удовлетворяет заданному условию signaturePredicateFunc.
## __См. также
#### Ссылки
[CardSignatureHelper - ](T_Tessa_Cards_CardSignatureHelper.htm)
[AnySignatureRow -
перегрузка](Overload_Tessa_Cards_CardSignatureHelper_AnySignatureRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
