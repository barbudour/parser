# CardTaskDialogHelper.GetCompletionOptionSettings(CardTask, Guid) - метод
Возвращает параметры диалога имеющие указанный идентификатор.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardTaskCompletionOptionSettings? GetCompletionOptionSettings(
    	CardTask task,
    	Guid completionOptionID
    )
VB __Копировать
     Public Shared Function GetCompletionOptionSettings ( 
    	task As CardTask,
    	completionOptionID As Guid
    ) As CardTaskCompletionOptionSettings
C++ __Копировать
     public:
    static CardTaskCompletionOptionSettings^ GetCompletionOptionSettings(
    	CardTask^ task, 
    	Guid completionOptionID
    )
F# __Копировать
     static member GetCompletionOptionSettings : 
            task : CardTask * 
            completionOptionID : Guid -> CardTaskCompletionOptionSettings 
#### Параметры
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Задание, содержащее параметры.
completionOptionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор варианта завершения.
#### Возвращаемое значение
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm)  
Параметры варианта завершения диалога или значение по умолчанию для типа, если
параметры не удалось получить.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[GetCompletionOptionSettings -
перегрузка](Overload_Tessa_Cards_CardTaskDialogHelper_GetCompletionOptionSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
