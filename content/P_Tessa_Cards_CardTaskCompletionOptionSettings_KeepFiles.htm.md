# CardTaskCompletionOptionSettings.KeepFiles - свойство
Возвращает или задаёт признак, нужно ли сохранять файлы после завершения
диалога или нет.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool KeepFiles { get; set; }
VB __Копировать
     Public Property KeepFiles As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool KeepFiles {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member KeepFiles : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Параметр актуален только для диалога с
[StoreMode](P_Tessa_Cards_CardTaskCompletionOptionSettings_StoreMode.htm)
равным [Settings](T_Tessa_Cards_CardTaskDialogStoreMode.htm).
## __См. также
#### Ссылки
[CardTaskCompletionOptionSettings -
](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
