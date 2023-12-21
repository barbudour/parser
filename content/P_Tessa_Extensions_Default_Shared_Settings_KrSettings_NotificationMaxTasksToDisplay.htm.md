# KrSettings.NotificationMaxTasksToDisplay - свойство
Максимальное количество новых заданий, которое отображается в отдельных окнах
уведомлений. Задания отображаются в порядке сортировки
[NotificationSortingColumnDirection](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationSortingColumnDirection.htm)
по колонке
[NotificationSortingColumnAlias](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationSortingColumnAlias.htm).
В настройках по умолчанию отображается первые несколько новых заданий. Полный
список заданий пользователь сможет посмотреть, если перейдёт в представление
[NotificationViewAlias](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationViewAlias.htm)
при клике по уведомлению с информацией по количеству заданий.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Settings](N_Tessa_Extensions_Default_Shared_Settings.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public int NotificationMaxTasksToDisplay { get; set; }
VB __Копировать
     Public Property NotificationMaxTasksToDisplay As Integer
    	Get
    	Set
C++ __Копировать
     public:
    property int NotificationMaxTasksToDisplay {
    	int get ();
    	void set (int value);
    }
F# __Копировать
     member NotificationMaxTasksToDisplay : int with get, set
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __См. также
#### Ссылки
[KrSettings - ](T_Tessa_Extensions_Default_Shared_Settings_KrSettings.htm)
[Tessa.Extensions.Default.Shared.Settings - пространство
имён](N_Tessa_Extensions_Default_Shared_Settings.htm)
