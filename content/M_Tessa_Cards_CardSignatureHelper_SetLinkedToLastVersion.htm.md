# CardSignatureHelper.SetLinkedToLastVersion - метод
Устанавливает признак того, что строка с ЭЦП связана с последней версией
файла, поэтому ссылка на идентификатор версии будет обновлена при сохранении
на случай, если для файла новая версия будет создана позже, чем была добавлена
подпись.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetLinkedToLastVersion(
    	CardRow signatureRow,
    	bool linkedToLastVersion = true
    )
VB __Копировать
     Public Shared Sub SetLinkedToLastVersion ( 
    	signatureRow As CardRow,
    	Optional linkedToLastVersion As Boolean = true
    )
C++ __Копировать
     public:
    static void SetLinkedToLastVersion(
    	CardRow^ signatureRow, 
    	bool linkedToLastVersion = true
    )
F# __Копировать
     static member SetLinkedToLastVersion : 
            signatureRow : CardRow * 
            ?linkedToLastVersion : bool 
    (* Defaults:
            let _linkedToLastVersion = defaultArg linkedToLastVersion true
    *)
    -> unit 
#### Параметры
signatureRow [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка с ЭЦП.
linkedToLastVersion
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что строка с ЭЦП связана с последней версией файла. 
## __См. также
#### Ссылки
[CardSignatureHelper - ](T_Tessa_Cards_CardSignatureHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
