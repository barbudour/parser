# KrSettingsLazy - конструктор
Инициализирует новый экземпляр класса
[KrSettingsLazy](T_Tessa_Extensions_Default_Shared_Settings_KrSettingsLazy.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Settings](N_Tessa_Extensions_Default_Shared_Settings.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrSettingsLazy(
    	Func<CancellationToken, ValueTask<KrSettings>> getSettingsFuncAsync
    )
VB __Копировать
     Public Sub New ( 
    	getSettingsFuncAsync As Func(Of CancellationToken, ValueTask(Of KrSettings))
    )
C++ __Копировать
     public:
    KrSettingsLazy(
    	Func<CancellationToken, ValueTask<KrSettings^>>^ getSettingsFuncAsync
    )
F# __Копировать
     new : 
            getSettingsFuncAsync : Func<CancellationToken, ValueTask<KrSettings>> -> KrSettingsLazy
#### Параметры
getSettingsFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[KrSettings](T_Tessa_Extensions_Default_Shared_Settings_KrSettings.htm)>>
## __См. также
#### Ссылки
[KrSettingsLazy -
](T_Tessa_Extensions_Default_Shared_Settings_KrSettingsLazy.htm)
[Tessa.Extensions.Default.Shared.Settings - пространство
имён](N_Tessa_Extensions_Default_Shared_Settings.htm)
