# KrSettings.GetMultiplePerformersDefaults - свойство
Функция, принимающая объект WfResolutionTaskInfo, описывающий задание, и
возвращающая режим по умолчанию для флажков, которые устанавливаются в задаче
при выборе нескольких исполнителей. Режим по умолчанию определяет лишь
начальное состояние флажков, пользователь может его изменить.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Settings](N_Tessa_Extensions_Default_Shared_Settings.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public Func<Object, WfMultiplePerformersDefaults> GetMultiplePerformersDefaults { get; set; }
VB __Копировать
     Public Property GetMultiplePerformersDefaults As Func(Of Object, WfMultiplePerformersDefaults)
    	Get
    	Set
C++ __Копировать
     public:
    property Func<Object^, WfMultiplePerformersDefaults>^ GetMultiplePerformersDefaults {
    	Func<Object^, WfMultiplePerformersDefaults>^ get ();
    	void set (Func<Object^, WfMultiplePerformersDefaults>^ value);
    }
F# __Копировать
     member GetMultiplePerformersDefaults : Func<Object, WfMultiplePerformersDefaults> with get, set
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[Object](https://learn.microsoft.com/dotnet/api/system.object),
[WfMultiplePerformersDefaults](T_Tessa_Extensions_Default_Shared_Settings_WfMultiplePerformersDefaults.htm)>
##  __См. также
#### Ссылки
[KrSettings - ](T_Tessa_Extensions_Default_Shared_Settings_KrSettings.htm)
[Tessa.Extensions.Default.Shared.Settings - пространство
имён](N_Tessa_Extensions_Default_Shared_Settings.htm)
