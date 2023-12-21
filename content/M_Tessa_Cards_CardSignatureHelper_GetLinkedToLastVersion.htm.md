# CardSignatureHelper.GetLinkedToLastVersion - метод
Возвращает признак того, что строка с ЭЦП связана с последней версией файла,
поэтому ссылка на идентификатор версии будет обновлена при сохранении на
случай, если для файла новая версия будет создана позже, чем была добавлена
подпись. Если признак не был установлен, то возвращается false.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool GetLinkedToLastVersion(
    	CardRow signatureRow
    )
VB __Копировать
     Public Shared Function GetLinkedToLastVersion ( 
    	signatureRow As CardRow
    ) As Boolean
C++ __Копировать
     public:
    static bool GetLinkedToLastVersion(
    	CardRow^ signatureRow
    )
F# __Копировать
     static member GetLinkedToLastVersion : 
            signatureRow : CardRow -> bool 
#### Параметры
signatureRow [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка с ЭЦП.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что строка с ЭЦП связана с последней версией файла. Если признак
не был установлен, то возвращается false.
## __См. также
#### Ссылки
[CardSignatureHelper - ](T_Tessa_Cards_CardSignatureHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
