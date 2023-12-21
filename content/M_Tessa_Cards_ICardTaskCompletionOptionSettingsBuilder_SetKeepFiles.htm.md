# ICardTaskCompletionOptionSettingsBuilder.SetKeepFiles - метод
Устанавливает значение флага "Сохранять файлы после завершения диалога".
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ICardTaskCompletionOptionSettingsBuilder SetKeepFiles(
    	bool keepFiles
    )
VB __Копировать
     Function SetKeepFiles ( 
    	keepFiles As Boolean
    ) As ICardTaskCompletionOptionSettingsBuilder
C++ __Копировать
    ICardTaskCompletionOptionSettingsBuilder^ SetKeepFiles(
    	bool keepFiles
    )
F# __Копировать
     abstract SetKeepFiles : 
            keepFiles : bool -> ICardTaskCompletionOptionSettingsBuilder 
#### Параметры
keepFiles [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение true, если файлы после завершения диалога не должны быть удалены, иначе - false.
#### Возвращаемое значение
[ICardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_ICardTaskCompletionOptionSettingsBuilder.htm)  
Текущий объект для создания цепочки вызовов.
##  __Заметки
Параметр актуален только для диалога с временем жизни
[Settings](T_Tessa_Cards_CardTaskDialogStoreMode.htm).
## __См. также
#### Ссылки
[ICardTaskCompletionOptionSettingsBuilder -
](T_Tessa_Cards_ICardTaskCompletionOptionSettingsBuilder.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
