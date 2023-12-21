# CardTaskCompletionOptionSettingsBuilder.SetKeepFiles - метод
Устанавливает значение флага "Сохранять файлы после завершения диалога".
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardTaskCompletionOptionSettingsBuilder SetKeepFiles(
    	bool keepFiles
    )
VB __Копировать
     Public Function SetKeepFiles ( 
    	keepFiles As Boolean
    ) As ICardTaskCompletionOptionSettingsBuilder
C++ __Копировать
     public:
    virtual ICardTaskCompletionOptionSettingsBuilder^ SetKeepFiles(
    	bool keepFiles
    ) sealed
F# __Копировать
     abstract SetKeepFiles : 
            keepFiles : bool -> ICardTaskCompletionOptionSettingsBuilder 
    override SetKeepFiles : 
            keepFiles : bool -> ICardTaskCompletionOptionSettingsBuilder 
#### Параметры
keepFiles [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение true, если файлы после завершения диалога не должны быть удалены, иначе - false.
#### Возвращаемое значение
[ICardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_ICardTaskCompletionOptionSettingsBuilder.htm)  
Текущий объект для создания цепочки вызовов.
#### Реализации
[ICardTaskCompletionOptionSettingsBuilder.SetKeepFiles(Boolean)](M_Tessa_Cards_ICardTaskCompletionOptionSettingsBuilder_SetKeepFiles.htm)  
##  __Заметки
Параметр актуален только для диалога с временем жизни
[Settings](T_Tessa_Cards_CardTaskDialogStoreMode.htm).
## __См. также
#### Ссылки
[CardTaskCompletionOptionSettingsBuilder -
](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
