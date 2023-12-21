# OpenInModalDialogOnDoubleClickExtension.Restore - метод
Осуществляет восстановление настроек расширения
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public void Restore(
    	Dictionary<string, Object> metadata
    )
VB __Копировать
     Public Sub Restore ( 
    	metadata As Dictionary(Of String, Object)
    )
C++ __Копировать
     public:
    virtual void Restore(
    	Dictionary<String^, Object^>^ metadata
    ) sealed
F# __Копировать
     abstract Restore : 
            metadata : Dictionary<string, Object> -> unit 
    override Restore : 
            metadata : Dictionary<string, Object> -> unit 
#### Параметры
metadata
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Сериализованные метаданные настроек 
#### Реализации
[IWorkplaceExtensionSettingsRestore.Restore(Dictionary<String,
Object>)](M_Tessa_UI_Views_Extensions_IWorkplaceExtensionSettingsRestore_Restore.htm)  
##  __См. также
#### Ссылки
[OpenInModalDialogOnDoubleClickExtension -
](T_Tessa_Extensions_Platform_Client_Cards_OpenInModalDialogOnDoubleClickExtension.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
