# CleanupFieldsSettingsCache.GetExtensionsSettingsAsync - метод
Возвращает набор с параметрами работы расширений на очситку стрк.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.CleanupFields](N_Tessa_Extensions_Platform_Client_UI_CleanupFields.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<CleanupFieldsTypeExtensionSettings> GetExtensionsSettingsAsync(
    	ITypeExtensionContext context
    )
VB __Копировать
     Public Function GetExtensionsSettingsAsync ( 
    	context As ITypeExtensionContext
    ) As ValueTask(Of CleanupFieldsTypeExtensionSettings)
C++ __Копировать
     public:
    ValueTask<CleanupFieldsTypeExtensionSettings^> GetExtensionsSettingsAsync(
    	ITypeExtensionContext^ context
    )
F# __Копировать
     member GetExtensionsSettingsAsync : 
            context : ITypeExtensionContext -> ValueTask<CleanupFieldsTypeExtensionSettings> 
#### Параметры
context [ITypeExtensionContext](T_Tessa_Cards_ITypeExtensionContext.htm)
    Контекст выполнения расширений на типах карточек
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CleanupFieldsTypeExtensionSettings](T_Tessa_Extensions_Platform_Client_UI_CleanupFields_CleanupFieldsTypeExtensionSettings.htm)>  
Набор с параметрами работы расширений
##  __См. также
#### Ссылки
[CleanupFieldsSettingsCache -
](T_Tessa_Extensions_Platform_Client_UI_CleanupFields_CleanupFieldsSettingsCache.htm)
[Tessa.Extensions.Platform.Client.UI.CleanupFields - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_CleanupFields.htm)
