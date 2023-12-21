# PreviewHandlersSelectorPool - конструктор
Инициализирует новый экземпляр класса
[PreviewHandlersSelectorPool](T_Tessa_PreviewHandlers_PreviewHandlersSelectorPool.htm)
##  __Definition
 **Пространство имён:** [Tessa.PreviewHandlers](N_Tessa_PreviewHandlers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public PreviewHandlersSelectorPool(
    	[DependencyAttribute("Preview32bit")] IPreviewHandlersPool pool32Bit,
    	[DependencyAttribute("Preview64bit")] IPreviewHandlersPool pool64Bit,
    	IPreviewHandlerSettings defaultSettings
    )
VB __Копировать
     Public Sub New ( 
    	<DependencyAttribute("Preview32bit")> pool32Bit As IPreviewHandlersPool,
    	<DependencyAttribute("Preview64bit")> pool64Bit As IPreviewHandlersPool,
    	defaultSettings As IPreviewHandlerSettings
    )
C++ __Копировать
     public:
    PreviewHandlersSelectorPool(
    	[DependencyAttribute(L"Preview32bit")] IPreviewHandlersPool^ pool32Bit, 
    	[DependencyAttribute(L"Preview64bit")] IPreviewHandlersPool^ pool64Bit, 
    	IPreviewHandlerSettings^ defaultSettings
    )
F# __Копировать
     new : 
            [<DependencyAttribute("Preview32bit")>] pool32Bit : IPreviewHandlersPool * 
            [<DependencyAttribute("Preview64bit")>] pool64Bit : IPreviewHandlersPool * 
            defaultSettings : IPreviewHandlerSettings -> PreviewHandlersSelectorPool
#### Параметры
pool32Bit
[IPreviewHandlersPool](T_Tessa_PreviewHandlers_IPreviewHandlersPool.htm)
pool64Bit
[IPreviewHandlersPool](T_Tessa_PreviewHandlers_IPreviewHandlersPool.htm)
defaultSettings
[IPreviewHandlerSettings](T_Tessa_PreviewHandlers_IPreviewHandlerSettings.htm)
## __См. также
#### Ссылки
[PreviewHandlersSelectorPool -
](T_Tessa_PreviewHandlers_PreviewHandlersSelectorPool.htm)
[Tessa.PreviewHandlers - пространство имён](N_Tessa_PreviewHandlers.htm)
