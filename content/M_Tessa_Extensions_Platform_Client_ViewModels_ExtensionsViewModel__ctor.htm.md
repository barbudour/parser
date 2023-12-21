# ExtensionsViewModel - конструктор
Инициализирует новый экземпляр класса
[ExtensionsViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_ExtensionsViewModel.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.ViewModels](N_Tessa_Extensions_Platform_Client_ViewModels.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ExtensionsViewModel(
    	IExtensionAssemblyInfo assemblyInfo,
    	IList<ITessaPatchInfo> patchList = null
    )
VB __Копировать
     Public Sub New ( 
    	assemblyInfo As IExtensionAssemblyInfo,
    	Optional patchList As IList(Of ITessaPatchInfo) = Nothing
    )
C++ __Копировать
     public:
    ExtensionsViewModel(
    	IExtensionAssemblyInfo^ assemblyInfo, 
    	IList<ITessaPatchInfo^>^ patchList = nullptr
    )
F# __Копировать
     new : 
            assemblyInfo : IExtensionAssemblyInfo * 
            ?patchList : IList<ITessaPatchInfo> 
    (* Defaults:
            let _patchList = defaultArg patchList null
    *)
    -> ExtensionsViewModel
#### Параметры
assemblyInfo
[IExtensionAssemblyInfo](T_Tessa_Extensions_IExtensionAssemblyInfo.htm)
patchList
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[ITessaPatchInfo](T_Tessa_Platform_ITessaPatchInfo.htm)>
(Optional)
## __См. также
#### Ссылки
[ExtensionsViewModel -
](T_Tessa_Extensions_Platform_Client_ViewModels_ExtensionsViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels - пространство
имён](N_Tessa_Extensions_Platform_Client_ViewModels.htm)
