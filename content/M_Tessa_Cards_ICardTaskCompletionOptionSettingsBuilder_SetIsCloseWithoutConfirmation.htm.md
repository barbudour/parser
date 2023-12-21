# ICardTaskCompletionOptionSettingsBuilder.SetIsCloseWithoutConfirmation -
метод
Устанавливает значение флага "Не предупреждать при закрытии диалога без
изменений".
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ICardTaskCompletionOptionSettingsBuilder SetIsCloseWithoutConfirmation(
    	bool isCloseWithoutConfirmation
    )
VB __Копировать
     Function SetIsCloseWithoutConfirmation ( 
    	isCloseWithoutConfirmation As Boolean
    ) As ICardTaskCompletionOptionSettingsBuilder
C++ __Копировать
    ICardTaskCompletionOptionSettingsBuilder^ SetIsCloseWithoutConfirmation(
    	bool isCloseWithoutConfirmation
    )
F# __Копировать
     abstract SetIsCloseWithoutConfirmation : 
            isCloseWithoutConfirmation : bool -> ICardTaskCompletionOptionSettingsBuilder 
#### Параметры
isCloseWithoutConfirmation
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение true, если при закрытии диалога без изменений не надо спрашивать подтверждение, иначе - false.
#### Возвращаемое значение
[ICardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_ICardTaskCompletionOptionSettingsBuilder.htm)  
Текущий объект для создания цепочки вызовов.
##  __Заметки
Параметр актуален только для диалога с временем жизни
[Info](T_Tessa_Cards_CardTaskDialogStoreMode.htm).
## __См. также
#### Ссылки
[ICardTaskCompletionOptionSettingsBuilder -
](T_Tessa_Cards_ICardTaskCompletionOptionSettingsBuilder.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
