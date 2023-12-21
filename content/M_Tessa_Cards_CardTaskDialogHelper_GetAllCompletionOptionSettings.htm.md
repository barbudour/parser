# CardTaskDialogHelper.GetAllCompletionOptionSettings - метод
Возвращает коллекцию содержащую информацию по всем параметрам диалога
содержащиеся в заданном задании.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IList<CardTaskCompletionOptionSettings> GetAllCompletionOptionSettings(
    	CardTask task
    )
VB __Копировать
     Public Shared Function GetAllCompletionOptionSettings ( 
    	task As CardTask
    ) As IList(Of CardTaskCompletionOptionSettings)
C++ __Копировать
     public:
    static IList<CardTaskCompletionOptionSettings^>^ GetAllCompletionOptionSettings(
    	CardTask^ task
    )
F# __Копировать
     static member GetAllCompletionOptionSettings : 
            task : CardTask -> IList<CardTaskCompletionOptionSettings> 
#### Параметры
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Задание.
#### Возвращаемое значение
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm)>  
Коллекция содержащая информацию по всем параметрам диалога содержащимся в
заданном задании.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
