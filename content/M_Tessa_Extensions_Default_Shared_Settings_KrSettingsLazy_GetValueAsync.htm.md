# KrSettingsLazy.GetValueAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Settings](N_Tessa_Extensions_Default_Shared_Settings.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<KrSettings> GetValueAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetValueAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of KrSettings)
C++ __Копировать
     public:
    ValueTask<KrSettings^> GetValueAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member GetValueAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<KrSettings> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[KrSettings](T_Tessa_Extensions_Default_Shared_Settings_KrSettings.htm)>
##  __См. также
#### Ссылки
[KrSettingsLazy -
](T_Tessa_Extensions_Default_Shared_Settings_KrSettingsLazy.htm)
[Tessa.Extensions.Default.Shared.Settings - пространство
имён](N_Tessa_Extensions_Default_Shared_Settings.htm)
