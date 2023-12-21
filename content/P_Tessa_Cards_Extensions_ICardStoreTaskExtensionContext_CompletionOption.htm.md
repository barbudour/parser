# ICardStoreTaskExtensionContext.CompletionOption - свойство
Вариант завершения задания или null, если вариант завершения неизвестен или
задание не завершается. Если задание завершается, т.е.
[Tessa.Cards.Extensions.ICardStoreTaskExtensionContext.IsCompletion] равен
true, то вариант завершения гарантированно не равен null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    CardMetadataCompletionOption CompletionOption { get; }
VB __Копировать
     ReadOnly Property CompletionOption As CardMetadataCompletionOption
    	Get
C++ __Копировать
    property CardMetadataCompletionOption^ CompletionOption {
    	CardMetadataCompletionOption^ get ();
    }
F# __Копировать
     abstract CompletionOption : CardMetadataCompletionOption with get
#### Значение свойства
[CardMetadataCompletionOption](T_Tessa_Cards_Metadata_CardMetadataCompletionOption.htm)
##  __См. также
#### Ссылки
[ICardStoreTaskExtensionContext -
](T_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
