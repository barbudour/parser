# ViewModel<TModel> \- класс
Базовый класс для моделей представления.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ViewModel<TModel> : NotificationUIObject, 
    	IViewModel, INotifyPropertyChanged, IWeakEventListener
VB __Копировать
     Public MustInherit Class ViewModel(Of TModel)
    	Inherits NotificationUIObject
    	Implements IViewModel, INotifyPropertyChanged, IWeakEventListener
C++ __Копировать
    generic<typename TModel>
    public ref class ViewModel abstract : public NotificationUIObject, 
    	IViewModel, INotifyPropertyChanged, IWeakEventListener
F# __Копировать
     [<AbstractClassAttribute>]
    type ViewModel<'TModel> = 
        class
            inherit NotificationUIObject
            interface IViewModel
            interface INotifyPropertyChanged
            interface IWeakEventListener
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __ ViewModel<TModel>
Derived
[Tessa.Extensions.Default.Client.Scanning.ServiceScanProvider](T_Tessa_Extensions_Default_Client_Scanning_ServiceScanProvider.htm)
[Tessa.Extensions.Default.Client.Scanning.ServiceScanSourceViewModel](T_Tessa_Extensions_Default_Client_Scanning_ServiceScanSourceViewModel.htm)
[Tessa.Extensions.Default.Client.Views.StageSelector.StageGroupViewModel](T_Tessa_Extensions_Default_Client_Views_StageSelector_StageGroupViewModel.htm)
[Tessa.Extensions.Default.Client.Views.StageSelector.StageSelectorViewModel](T_Tessa_Extensions_Default_Client_Views_StageSelector_StageSelectorViewModel.htm)
[Tessa.Extensions.Default.Client.Views.StageSelector.StageTypeViewModel](T_Tessa_Extensions_Default_Client_Views_StageSelector_StageTypeViewModel.htm)
[Tessa.Extensions.Default.Client.Workplaces.AutomaticNodeRefreshExtension](T_Tessa_Extensions_Default_Client_Workplaces_AutomaticNodeRefreshExtension.htm)
[Tessa.Extensions.Default.Client.Workplaces.Manager.ManagerWorkplaceTilesViewModel](T_Tessa_Extensions_Default_Client_Workplaces_Manager_ManagerWorkplaceTilesViewModel.htm)
[Tessa.Extensions.Default.Client.Workplaces.RefSectionExtension](T_Tessa_Extensions_Default_Client_Workplaces_RefSectionExtension.htm)
[Tessa.Extensions.Default.Client.Workplaces.WebChart.Palette.PaletteSelectorViewModel](T_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette_PaletteSelectorViewModel.htm)
[Tessa.Extensions.Default.Client.Workplaces.WebChart.WebChartColorPickerViewModel](T_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartColorPickerViewModel.htm)
[Tessa.Extensions.Default.Client.Workplaces.WebChart.WebChartSettingsViewModel](T_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel.htm)
[Tessa.Extensions.Platform.Client.Scanning.FakeScanProvider](T_Tessa_Extensions_Platform_Client_Scanning_FakeScanProvider.htm)
[Tessa.Extensions.Platform.Client.UI.TaskHistory.TaskHistoryViewDetailsElementViewModel](T_Tessa_Extensions_Platform_Client_UI_TaskHistory_TaskHistoryViewDetailsElementViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TaskHistory.TaskHistoryViewDetailsViewModel](T_Tessa_Extensions_Platform_Client_UI_TaskHistory_TaskHistoryViewDetailsViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels.ConfigurationInfoDialogViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_ConfigurationInfoDialogViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels.ExtensionsViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_ExtensionsViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels.ScanDocumentTypeViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_ScanDocumentTypeViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels.ScanPageViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_ScanPageViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels.TabViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_TabViewModel.htm)
[Tessa.UI.AppManager.About.AboutCatalogViewModel](T_Tessa_UI_AppManager_About_AboutCatalogViewModel.htm)
[Tessa.UI.AppManager.About.AboutViewModel](T_Tessa_UI_AppManager_About_AboutViewModel.htm)
[Tessa.UI.AppManager.About.LicenseModuleLinkViewModel](T_Tessa_UI_AppManager_About_LicenseModuleLinkViewModel.htm)
[Tessa.UI.AppManager.ApplicationsButtonsViewModel](T_Tessa_UI_AppManager_ApplicationsButtonsViewModel.htm)
[Tessa.UI.AppManager.CatalogService.ApplicationCatalog](T_Tessa_UI_AppManager_CatalogService_ApplicationCatalog.htm)
[Tessa.UI.AppManager.CatalogService.ApplicationCatalogManagerViewModel](T_Tessa_UI_AppManager_CatalogService_ApplicationCatalogManagerViewModel.htm)
[Tessa.UI.AppManager.CatalogService.ApplicationCatalogRegistry](T_Tessa_UI_AppManager_CatalogService_ApplicationCatalogRegistry.htm)
[Tessa.UI.AppManager.CatalogService.ApplicationCatalogViewModel](T_Tessa_UI_AppManager_CatalogService_ApplicationCatalogViewModel.htm)
[Tessa.UI.AppManager.CatalogService.ApplicationsViewModel](T_Tessa_UI_AppManager_CatalogService_ApplicationsViewModel.htm)
[Tessa.UI.AppManager.CatalogService.ApplicationViewModel](T_Tessa_UI_AppManager_CatalogService_ApplicationViewModel.htm)
[Tessa.UI.AppManager.CatalogService.ConnectionStateViewModel](T_Tessa_UI_AppManager_CatalogService_ConnectionStateViewModel.htm)
[Tessa.UI.AppManager.CatalogService.EditableApplicationCatalogViewModel](T_Tessa_UI_AppManager_CatalogService_EditableApplicationCatalogViewModel.htm)
[Tessa.UI.AppManager.GroupingViewModel](T_Tessa_UI_AppManager_GroupingViewModel.htm)
[Tessa.UI.AppManager.ShellPagesControllerViewModel](T_Tessa_UI_AppManager_ShellPagesControllerViewModel.htm)
[Tessa.UI.AppManager.ShellPageViewModel](T_Tessa_UI_AppManager_ShellPageViewModel.htm)
[Tessa.UI.AppManager.ShellViewModel](T_Tessa_UI_AppManager_ShellViewModel.htm)
[Tessa.UI.Automation.AutomationViewModel<TModel>](T_Tessa_UI_Automation_AutomationViewModel_1.htm)
[Tessa.UI.Cards.Models.CardLibraryImportDialogModel](T_Tessa_UI_Cards_Models_CardLibraryImportDialogModel.htm)
[Tessa.UI.Cards.Models.CardLibraryItemModel](T_Tessa_UI_Cards_Models_CardLibraryItemModel.htm)
[Tessa.UI.Cards.Models.CardLibraryTemplateDialogModel](T_Tessa_UI_Cards_Models_CardLibraryTemplateDialogModel.htm)
[Tessa.UI.Cards.Models.CardRowFormViewModel](T_Tessa_UI_Cards_Models_CardRowFormViewModel.htm)
[Tessa.UI.Cards.Tasks.TaskHistoryItemDetailsViewModel](T_Tessa_UI_Cards_Tasks_TaskHistoryItemDetailsViewModel.htm)
[Tessa.UI.Cards.Types.CardMetadataCompletionOptionViewModel](T_Tessa_UI_Cards_Types_CardMetadataCompletionOptionViewModel.htm)
[Tessa.UI.Cards.Types.CardTypeObjectViewModel<TModel>](T_Tessa_UI_Cards_Types_CardTypeObjectViewModel_1.htm)
[Tessa.UI.Cards.Types.CardTypeTabViewModel](T_Tessa_UI_Cards_Types_CardTypeTabViewModel.htm)
[Tessa.UI.Controls.ColorPalette.ButtonPaletteItemViewModel](T_Tessa_UI_Controls_ColorPalette_ButtonPaletteItemViewModel.htm)
[Tessa.UI.Controls.ColorPalette.ColorPaletteItemViewModel](T_Tessa_UI_Controls_ColorPalette_ColorPaletteItemViewModel.htm)
[Tessa.UI.Controls.ColorPalette.ColorPaletteViewModel](T_Tessa_UI_Controls_ColorPalette_ColorPaletteViewModel.htm)
[Tessa.UI.Controls.ColorPalette.DropDownColorPickerViewModel](T_Tessa_UI_Controls_ColorPalette_DropDownColorPickerViewModel.htm)
[Tessa.UI.Controls.CustomRichTextBoxCtrl.AddFilesButtonViewModel](T_Tessa_UI_Controls_CustomRichTextBoxCtrl_AddFilesButtonViewModel.htm)
[Tessa.UI.Controls.CustomRichTextBoxCtrl.BlRichTextBoxViewModelBase](T_Tessa_UI_Controls_CustomRichTextBoxCtrl_BlRichTextBoxViewModelBase.htm)
[Tessa.UI.Controls.CustomRichTextBoxCtrl.ImageWindowViewModel](T_Tessa_UI_Controls_CustomRichTextBoxCtrl_ImageWindowViewModel.htm)
[Tessa.UI.Controls.CustomRichTextBoxCtrl.ItemBaseViewModel](T_Tessa_UI_Controls_CustomRichTextBoxCtrl_ItemBaseViewModel.htm)
[Tessa.UI.Controls.FilePreview.PagingPreviewViewModel](T_Tessa_UI_Controls_FilePreview_PagingPreviewViewModel.htm)
[Tessa.UI.Controls.Forums.ForumControlContentViewModelBase<T>](T_Tessa_UI_Controls_Forums_ForumControlContentViewModelBase_1.htm)
[Tessa.UI.Controls.Forums.ForumSearchBoxViewModel](T_Tessa_UI_Controls_Forums_ForumSearchBoxViewModel.htm)
[Tessa.UI.Controls.Forums.ForumViewModel](T_Tessa_UI_Controls_Forums_ForumViewModel.htm)
[Tessa.UI.Controls.Forums.MenuControlViewModelBase<TModel>](T_Tessa_UI_Controls_Forums_MenuControlViewModelBase_1.htm)
[Tessa.UI.Controls.Forums.MessageMenuViewModelBase](T_Tessa_UI_Controls_Forums_MessageMenuViewModelBase.htm)
[Tessa.UI.Controls.Forums.MessageViewModelBase](T_Tessa_UI_Controls_Forums_MessageViewModelBase.htm)
[Tessa.UI.Controls.Forums.NotificationItemsViewModel](T_Tessa_UI_Controls_Forums_NotificationItemsViewModel.htm)
[Tessa.UI.Controls.Forums.NotificationItemViewModelBase](T_Tessa_UI_Controls_Forums_NotificationItemViewModelBase.htm)
[Tessa.UI.Controls.Forums.TopicViewModelBase](T_Tessa_UI_Controls_Forums_TopicViewModelBase.htm)
[Tessa.UI.Controls.GridColumnSelectorViewModel](T_Tessa_UI_Controls_GridColumnSelectorViewModel.htm)
[Tessa.UI.Controls.GridColumnViewModel](T_Tessa_UI_Controls_GridColumnViewModel.htm)
[Tessa.UI.Controls.ItemsControlViewModel<TItemModel,
TItemViewModel>](T_Tessa_UI_Controls_ItemsControlViewModel_2.htm)
[Tessa.UI.Controls.ListSelector.ListSelectorViewModel](T_Tessa_UI_Controls_ListSelector_ListSelectorViewModel.htm)
[Tessa.UI.Controls.Scrolling.ScrollingButtonViewModel](T_Tessa_UI_Controls_Scrolling_ScrollingButtonViewModel.htm)
[Tessa.UI.Controls.Scrolling.ScrollingControlViewModel](T_Tessa_UI_Controls_Scrolling_ScrollingControlViewModel.htm)
[Tessa.UI.Controls.Scrolling.ScrollingPageViewModel](T_Tessa_UI_Controls_Scrolling_ScrollingPageViewModel.htm)
[Tessa.UI.Controls.SelectParamViewModel](T_Tessa_UI_Controls_SelectParamViewModel.htm)
[Tessa.UI.Controls.TessaGrid.TessaGridColumnViewModel](T_Tessa_UI_Controls_TessaGrid_TessaGridColumnViewModel.htm)
[Tessa.UI.Controls.ValidationResultDialogViewModel](T_Tessa_UI_Controls_ValidationResultDialogViewModel.htm)
[Tessa.UI.Controls.ValidationResultViewModel](T_Tessa_UI_Controls_ValidationResultViewModel.htm)
[Tessa.UI.Controls.ViewMapper.ViewMapperViewModel](T_Tessa_UI_Controls_ViewMapper_ViewMapperViewModel.htm)
[Tessa.UI.Controls.ViewMapper.ViewMapping](T_Tessa_UI_Controls_ViewMapper_ViewMapping.htm)
[Tessa.UI.Controls.Workflow.CardBindingEditorViewModel](T_Tessa_UI_Controls_Workflow_CardBindingEditorViewModel.htm)
[Tessa.UI.Controls.Workflow.HashBindingEditorViewModel](T_Tessa_UI_Controls_Workflow_HashBindingEditorViewModel.htm)
[Tessa.UI.Controls.Workflow.SqlBindingEditorViewModel](T_Tessa_UI_Controls_Workflow_SqlBindingEditorViewModel.htm)
[Tessa.UI.Controls.Workflow.TaskBindingEditorViewModel](T_Tessa_UI_Controls_Workflow_TaskBindingEditorViewModel.htm)
[Tessa.UI.Controls.Workflow.ViewBindingEditorViewModel](T_Tessa_UI_Controls_Workflow_ViewBindingEditorViewModel.htm)
[Tessa.UI.Diagnostics.PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm)
[Tessa.UI.Differences.SubmittingQueueItemViewModel<TModel,
TObjectModel>](T_Tessa_UI_Differences_SubmittingQueueItemViewModel_2.htm)
[Tessa.UI.EditableViewModel<TModel>](T_Tessa_UI_EditableViewModel_1.htm)
[Tessa.UI.Files.Controls.CommentDialog.CommentDialogViewModel](T_Tessa_UI_Files_Controls_CommentDialog_CommentDialogViewModel.htm)
[Tessa.UI.Files.Controls.DigitalSignature.FileSignatureViewModel](T_Tessa_UI_Files_Controls_DigitalSignature_FileSignatureViewModel.htm)
[Tessa.UI.Files.Controls.FileCategoryTypeSelector.FileCategoryTypeSelectorViewModel<T>](T_Tessa_UI_Files_Controls_FileCategoryTypeSelector_FileCategoryTypeSelectorViewModel_1.htm)
[Tessa.UI.Files.Controls.RenameDialog.FileRenameDialogViewModel](T_Tessa_UI_Files_Controls_RenameDialog_FileRenameDialogViewModel.htm)
[Tessa.UI.Files.FileControlObject](T_Tessa_UI_Files_FileControlObject.htm)
[Tessa.UI.Files.FileTagViewModel](T_Tessa_UI_Files_FileTagViewModel.htm)
[Tessa.UI.HashEditor.Editors.KeyEditorViewModel](T_Tessa_UI_HashEditor_Editors_KeyEditorViewModel.htm)
[Tessa.UI.HashEditor.Editors.TypeSelectorViewModel](T_Tessa_UI_HashEditor_Editors_TypeSelectorViewModel.htm)
[Tessa.UI.HashEditor.Editors.ValueEditorViewModel](T_Tessa_UI_HashEditor_Editors_ValueEditorViewModel.htm)
[Tessa.UI.HashEditor.Hash.HashNode](T_Tessa_UI_HashEditor_Hash_HashNode.htm)
[Tessa.UI.HashEditor.HashEditorViewModel](T_Tessa_UI_HashEditor_HashEditorViewModel.htm)
[Tessa.UI.HashEditor.InputValueViewModel](T_Tessa_UI_HashEditor_InputValueViewModel.htm)
[Tessa.UI.Localization.CultureInfoViewModel](T_Tessa_UI_Localization_CultureInfoViewModel.htm)
[Tessa.UI.Localization.LocalizationEditorViewModel](T_Tessa_UI_Localization_LocalizationEditorViewModel.htm)
[Tessa.UI.Scheme.Filter.FilterObject](T_Tessa_UI_Scheme_Filter_FilterObject.htm)
[Tessa.UI.Scheme.Legacy.TableAndColumnSelectorViewModel](T_Tessa_UI_Scheme_Legacy_TableAndColumnSelectorViewModel.htm)
[Tessa.UI.Scheme.Providers.Database.ConnectionDialogViewModel](T_Tessa_UI_Scheme_Providers_Database_ConnectionDialogViewModel.htm)
[Tessa.UI.Scheme.Providers.Database.ConnectionSettingsViewModel](T_Tessa_UI_Scheme_Providers_Database_ConnectionSettingsViewModel.htm)
[Tessa.UI.Scheme.Providers.File.OpenSchemeDialogViewModel](T_Tessa_UI_Scheme_Providers_File_OpenSchemeDialogViewModel.htm)
[Tessa.UI.Scheme.Providers.ObjectPropertiesViewModel](T_Tessa_UI_Scheme_Providers_ObjectPropertiesViewModel.htm)
[Tessa.UI.Scheme.ReferencingColumnExistanceViewModel](T_Tessa_UI_Scheme_ReferencingColumnExistanceViewModel.htm)
[Tessa.UI.Scheme.SchemeEditorViewModel](T_Tessa_UI_Scheme_SchemeEditorViewModel.htm)
[Tessa.UI.SelectableViewModel<TModel>](T_Tessa_UI_SelectableViewModel_1.htm)
[Tessa.UI.Views.AccessDeniedViewComponent](T_Tessa_UI_Views_AccessDeniedViewComponent.htm)
[Tessa.UI.Views.Charting.Annotations.AnnotationEditorViewModel](T_Tessa_UI_Views_Charting_Annotations_AnnotationEditorViewModel.htm)
[Tessa.UI.Views.Charting.Axises.AxisEditorViewModel](T_Tessa_UI_Views_Charting_Axises_AxisEditorViewModel.htm)
[Tessa.UI.Views.Charting.Axises.StripLineLabel](T_Tessa_UI_Views_Charting_Axises_StripLineLabel.htm)
[Tessa.UI.Views.Charting.Behaviors.BehaviorsEditorViewModel](T_Tessa_UI_Views_Charting_Behaviors_BehaviorsEditorViewModel.htm)
[Tessa.UI.Views.Charting.Charts.Chart2DViewModel](T_Tessa_UI_Views_Charting_Charts_Chart2DViewModel.htm)
[Tessa.UI.Views.Charting.Charts.ChartEditorContext](T_Tessa_UI_Views_Charting_Charts_ChartEditorContext.htm)
[Tessa.UI.Views.Charting.Charts.ChartsViewModel](T_Tessa_UI_Views_Charting_Charts_ChartsViewModel.htm)
[Tessa.UI.Views.Charting.Charts.ToolbarViewModel](T_Tessa_UI_Views_Charting_Charts_ToolbarViewModel.htm)
[Tessa.UI.Views.Charting.ContextualViewModel<TModel>](T_Tessa_UI_Views_Charting_ContextualViewModel_1.htm)
[Tessa.UI.Views.Charting.Controls.AppearanceEditorViewModel](T_Tessa_UI_Views_Charting_Controls_AppearanceEditorViewModel.htm)
[Tessa.UI.Views.Charting.Controls.ColumnsSelectorViewModel](T_Tessa_UI_Views_Charting_Controls_ColumnsSelectorViewModel.htm)
[Tessa.UI.Views.Charting.Controls.EnumFlagsSelectorViewModel](T_Tessa_UI_Views_Charting_Controls_EnumFlagsSelectorViewModel.htm)
[Tessa.UI.Views.Charting.Controls.EnumValueDecorator](T_Tessa_UI_Views_Charting_Controls_EnumValueDecorator.htm)
[Tessa.UI.Views.Charting.Controls.ItemSelectorViewModel<TModel,
TValue>](T_Tessa_UI_Views_Charting_Controls_ItemSelectorViewModel_2.htm)
[Tessa.UI.Views.Charting.Controls.TimeSpanEditorViewModel](T_Tessa_UI_Views_Charting_Controls_TimeSpanEditorViewModel.htm)
[Tessa.UI.Views.Charting.Dashboard.DashboardDesignerViewModel](T_Tessa_UI_Views_Charting_Dashboard_DashboardDesignerViewModel.htm)
[Tessa.UI.Views.Charting.Layout.GridLayoutCollectionEditorViewModel](T_Tessa_UI_Views_Charting_Layout_GridLayoutCollectionEditorViewModel.htm)
[Tessa.UI.Views.Charting.Layout.GridLayoutEditorViewModel](T_Tessa_UI_Views_Charting_Layout_GridLayoutEditorViewModel.htm)
[Tessa.UI.Views.Charting.Legends.LegendEditorViewModel](T_Tessa_UI_Views_Charting_Legends_LegendEditorViewModel.htm)
[Tessa.UI.Views.Charting.Legends.LegendSelectorViewModel](T_Tessa_UI_Views_Charting_Legends_LegendSelectorViewModel.htm)
[Tessa.UI.Views.Charting.Legends.LegendSettingsViewModel](T_Tessa_UI_Views_Charting_Legends_LegendSettingsViewModel.htm)
[Tessa.UI.Views.Charting.Palettes.PaletteSelectorViewModel](T_Tessa_UI_Views_Charting_Palettes_PaletteSelectorViewModel.htm)
[Tessa.UI.Views.Charting.Properties.Property<TModel,
TValue>](T_Tessa_UI_Views_Charting_Properties_Property_2.htm)
[Tessa.UI.Views.Charting.Properties.PropertyContainer<TModel>](T_Tessa_UI_Views_Charting_Properties_PropertyContainer_1.htm)
[Tessa.UI.Views.Charting.Series.ChartSeriesEditorViewModel](T_Tessa_UI_Views_Charting_Series_ChartSeriesEditorViewModel.htm)
[Tessa.UI.Views.Charting.ToolboxViewModel](T_Tessa_UI_Views_Charting_ToolboxViewModel.htm)
[Tessa.UI.Views.Charting.Widgets.WidgetBoxItem](T_Tessa_UI_Views_Charting_Widgets_WidgetBoxItem.htm)
[Tessa.UI.Views.Charting.Widgets.WidgetBoxViewModel](T_Tessa_UI_Views_Charting_Widgets_WidgetBoxViewModel.htm)
[Tessa.UI.Views.Charting.Widgets.WidgetDecoratorViewModel](T_Tessa_UI_Views_Charting_Widgets_WidgetDecoratorViewModel.htm)
[Tessa.UI.Views.Content.BaseContentItem](T_Tessa_UI_Views_Content_BaseContentItem.htm)
[Tessa.UI.Views.Content.ContentProvider](T_Tessa_UI_Views_Content_ContentProvider.htm)
[Tessa.UI.Views.Content.Table.GridViewModelBase](T_Tessa_UI_Views_Content_Table_GridViewModelBase.htm)
[Tessa.UI.Views.Content.ViewControlMultiTagViewModel](T_Tessa_UI_Views_Content_ViewControlMultiTagViewModel.htm)
[Tessa.UI.Views.Content.ViewControlTagViewModel](T_Tessa_UI_Views_Content_ViewControlTagViewModel.htm)
[Tessa.UI.Views.Filtering.FilterAutoCompleteDataSource](T_Tessa_UI_Views_Filtering_FilterAutoCompleteDataSource.htm)
[Tessa.UI.Views.Filtering.FilterCriteriaViewModel](T_Tessa_UI_Views_Filtering_FilterCriteriaViewModel.htm)
[Tessa.UI.Views.Filtering.FilterEditorBaseViewModel](T_Tessa_UI_Views_Filtering_FilterEditorBaseViewModel.htm)
[Tessa.UI.Views.Filtering.FilterItemViewModel](T_Tessa_UI_Views_Filtering_FilterItemViewModel.htm)
[Tessa.UI.Views.Filtering.FilterViewModel](T_Tessa_UI_Views_Filtering_FilterViewModel.htm)
[Tessa.UI.Views.Filtering.ViewModels.RequestCriteriaViewModel](T_Tessa_UI_Views_Filtering_ViewModels_RequestCriteriaViewModel.htm)
[Tessa.UI.Views.Parameters.ViewParametersSwitcher](T_Tessa_UI_Views_Parameters_ViewParametersSwitcher.htm)
[Tessa.UI.Views.SearchQueriesViewModel](T_Tessa_UI_Views_SearchQueriesViewModel.htm)
[Tessa.UI.Views.SearchQueryDialogViewModel](T_Tessa_UI_Views_SearchQueryDialogViewModel.htm)
[Tessa.UI.Views.SearchQueryManageDialogViewModel](T_Tessa_UI_Views_SearchQueryManageDialogViewModel.htm)
[Tessa.UI.Views.SearchQueryViewModel](T_Tessa_UI_Views_SearchQueryViewModel.htm)
[Tessa.UI.Views.SectionSearchQueryViewModel](T_Tessa_UI_Views_SectionSearchQueryViewModel.htm)
[Tessa.UI.Views.ViewPaging.ViewPagingContentItem](T_Tessa_UI_Views_ViewPaging_ViewPagingContentItem.htm)
[Tessa.UI.Views.WorkplaceLayoutViewModel](T_Tessa_UI_Views_WorkplaceLayoutViewModel.htm)
[Tessa.UI.Views.Workplaces.OpenedCardObserver](T_Tessa_UI_Views_Workplaces_OpenedCardObserver.htm)
[Tessa.UI.Views.Workplaces.Tree.TreeItemHeader<TTreeItemHeader>](T_Tessa_UI_Views_Workplaces_Tree_TreeItemHeader_1.htm)
[Tessa.UI.Views.WorkplaceViewComponent](T_Tessa_UI_Views_WorkplaceViewComponent.htm)
[Tessa.UI.WorkflowViewer.Editor.EditorComponentBase](T_Tessa_UI_WorkflowViewer_Editor_EditorComponentBase.htm)
[Tessa.UI.WorkflowViewer.ExtendedNodeContent](T_Tessa_UI_WorkflowViewer_ExtendedNodeContent.htm)
[Tessa.UI.WorkflowViewer.Layouts.NodeLayout](T_Tessa_UI_WorkflowViewer_Layouts_NodeLayout.htm)
[Tessa.UI.WorkflowViewer.ViewModels.WorkflowEditorViewModel](T_Tessa_UI_WorkflowViewer_ViewModels_WorkflowEditorViewModel.htm)
[Tessa.UI.WorkflowViewer.ViewModels.WorkflowFilterRowViewModel](T_Tessa_UI_WorkflowViewer_ViewModels_WorkflowFilterRowViewModel.htm)
[Tessa.UI.WorkflowViewer.ViewModels.WorkflowInEditorBaseViewModel<T>](T_Tessa_UI_WorkflowViewer_ViewModels_WorkflowInEditorBaseViewModel_1.htm)
[Tessa.UI.WorkflowViewer.ViewModels.WorkflowNodeAdditionalViewModel](T_Tessa_UI_WorkflowViewer_ViewModels_WorkflowNodeAdditionalViewModel.htm)
[Tessa.UI.WorkflowViewer.ViewModels.WorkflowNodeContentViewModel](T_Tessa_UI_WorkflowViewer_ViewModels_WorkflowNodeContentViewModel.htm)
[Tessa.UI.WorkflowViewer.ViewModels.WorkflowSignalViewModel](T_Tessa_UI_WorkflowViewer_ViewModels_WorkflowSignalViewModel.htm)
Подробнее __Less __
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IWeakEventListener](https://learn.microsoft.com/dotnet/api/system.windows.iweakeventlistener), [IViewModel](T_Tessa_UI_IViewModel.htm)
#### Параметры типа
TModel
##  __Конструкторы
[ViewModel<TModel>()](M_Tessa_UI_ViewModel_1__ctor.htm)| Инициализирует новый
экземпляр класса ViewModel<TModel>  
---|---  
[ViewModel<TModel>(TModel)](M_Tessa_UI_ViewModel_1__ctor_2.htm)|
Инициализирует новый экземпляр класса ViewModel<TModel>  
[ViewModel<TModel>(ViewModelScope)](M_Tessa_UI_ViewModel_1__ctor_1.htm)|
Инициализирует новый экземпляр класса ViewModel<TModel>  
[ViewModel<TModel>(TModel,
ViewModelScope)](M_Tessa_UI_ViewModel_1__ctor_3.htm)| Инициализирует новый
экземпляр класса ViewModel<TModel>  
##  __Свойства
[Model](P_Tessa_UI_ViewModel_1_Model.htm)|  Модель для текущей модели
представления.  
---|---  
[Scope](P_Tessa_UI_ViewModel_1_Scope.htm)|  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnModelPropertyChanged](M_Tessa_UI_ViewModel_1_OnModelPropertyChanged.htm)|  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Platform_NotificationObject_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChanged(String)](M_Tessa_Platform_NotificationObject_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs,
Boolean)](M_Tessa_UI_NotificationUIObject_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm))  
[OnPropertyChangedAsync(String,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnReceiveWeakEvent](M_Tessa_UI_ViewModel_1_OnReceiveWeakEvent.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
---|---  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
