# CardTaskDialogHelper.SetCardTaskDialogActionResult(IDictionary<String,
Object>, CardTaskDialogActionResult) - метод
Задаёт информацию о завершении диалога.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetCardTaskDialogActionResult(
    	IDictionary<string, Object?> storage,
    	CardTaskDialogActionResult? actionResult
    )
VB __Копировать
     Public Shared Sub SetCardTaskDialogActionResult ( 
    	storage As IDictionary(Of String, Object),
    	actionResult As CardTaskDialogActionResult
    )
C++ __Копировать
     public:
    static void SetCardTaskDialogActionResult(
    	IDictionary<String^, Object^>^ storage, 
    	CardTaskDialogActionResult^ actionResult
    )
F# __Копировать
     static member SetCardTaskDialogActionResult : 
            storage : IDictionary<string, Object> * 
            actionResult : CardTaskDialogActionResult -> unit 
#### Параметры
storage
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Коллекция ключ-значение, в котором должна быть сохранена информация о завершении диалога.
actionResult
[CardTaskDialogActionResult](T_Tessa_Cards_CardTaskDialogActionResult.htm)
    Информация о завершении диалога. Может иметь значение null.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[SetCardTaskDialogActionResult -
перегрузка](Overload_Tessa_Cards_CardTaskDialogHelper_SetCardTaskDialogActionResult.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
