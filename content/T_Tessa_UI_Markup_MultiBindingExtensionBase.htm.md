# MultiBindingExtensionBase - класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Markup](N_Tessa_UI_Markup.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
    [ContentPropertyAttribute("Bindings")]
    public abstract class MultiBindingExtensionBase : BindingBaseExtensionBase, 
    	IAddChild
VB __Копировать
    <ContentPropertyAttribute("Bindings")>
    Public MustInherit Class MultiBindingExtensionBase
    	Inherits BindingBaseExtensionBase
    	Implements IAddChild
C++ __Копировать
    [ContentPropertyAttribute(L"Bindings")]
    public ref class MultiBindingExtensionBase abstract : public BindingBaseExtensionBase, 
    	IAddChild
F# __Копировать
     [<AbstractClassAttribute>]
    [<ContentPropertyAttribute("Bindings")>]
    type MultiBindingExtensionBase = 
        class
            inherit BindingBaseExtensionBase
            interface IAddChild
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[MarkupExtension](https://learn.microsoft.com/dotnet/api/system.windows.markup.markupextension) __[BindingBaseExtensionBase](T_Tessa_UI_Markup_BindingBaseExtensionBase.htm) __ MultiBindingExtensionBase
Derived
[Tessa.UI.Markup.DelayMultiBindingExtension](T_Tessa_UI_Markup_DelayMultiBindingExtension.htm)
Implements
    [IAddChild](https://learn.microsoft.com/dotnet/api/system.windows.markup.iaddchild)
##  __Конструкторы
[MultiBindingExtensionBase](M_Tessa_UI_Markup_MultiBindingExtensionBase__ctor.htm)|
Инициализирует новый экземпляр класса MultiBindingExtensionBase  
---|---  
##  __Свойства
[BindingBase](P_Tessa_UI_Markup_MultiBindingExtensionBase_BindingBase.htm)|  
(Переопределяет
[BindingBaseExtensionBase.BindingBase](P_Tessa_UI_Markup_BindingBaseExtensionBase_BindingBase.htm))  
---|---  
[BindingGroupName](P_Tessa_UI_Markup_BindingBaseExtensionBase_BindingGroupName.htm)|  
(Унаследован от
[BindingBaseExtensionBase](T_Tessa_UI_Markup_BindingBaseExtensionBase.htm))  
[Bindings](P_Tessa_UI_Markup_MultiBindingExtensionBase_Bindings.htm)|  
[Converter](P_Tessa_UI_Markup_MultiBindingExtensionBase_Converter.htm)|  
[ConverterCulture](P_Tessa_UI_Markup_MultiBindingExtensionBase_ConverterCulture.htm)|  
[ConverterParameter](P_Tessa_UI_Markup_MultiBindingExtensionBase_ConverterParameter.htm)|  
[FallbackValue](P_Tessa_UI_Markup_BindingBaseExtensionBase_FallbackValue.htm)|  
(Унаследован от
[BindingBaseExtensionBase](T_Tessa_UI_Markup_BindingBaseExtensionBase.htm))  
[Mode](P_Tessa_UI_Markup_MultiBindingExtensionBase_Mode.htm)|  
[MultiBinding](P_Tessa_UI_Markup_MultiBindingExtensionBase_MultiBinding.htm)|  
[NotifyOnSourceUpdated](P_Tessa_UI_Markup_MultiBindingExtensionBase_NotifyOnSourceUpdated.htm)|  
[NotifyOnTargetUpdated](P_Tessa_UI_Markup_MultiBindingExtensionBase_NotifyOnTargetUpdated.htm)|  
[NotifyOnValidationError](P_Tessa_UI_Markup_MultiBindingExtensionBase_NotifyOnValidationError.htm)|  
[StringFormat](P_Tessa_UI_Markup_BindingBaseExtensionBase_StringFormat.htm)|  
(Унаследован от
[BindingBaseExtensionBase](T_Tessa_UI_Markup_BindingBaseExtensionBase.htm))  
[TargetNullValue](P_Tessa_UI_Markup_BindingBaseExtensionBase_TargetNullValue.htm)|  
(Унаследован от
[BindingBaseExtensionBase](T_Tessa_UI_Markup_BindingBaseExtensionBase.htm))  
[UpdateSourceExceptionFilter](P_Tessa_UI_Markup_MultiBindingExtensionBase_UpdateSourceExceptionFilter.htm)|  
[UpdateSourceTrigger](P_Tessa_UI_Markup_MultiBindingExtensionBase_UpdateSourceTrigger.htm)|  
[ValidatesOnDataErrors](P_Tessa_UI_Markup_MultiBindingExtensionBase_ValidatesOnDataErrors.htm)|  
[ValidatesOnExceptions](P_Tessa_UI_Markup_MultiBindingExtensionBase_ValidatesOnExceptions.htm)|  
[ValidationRules](P_Tessa_UI_Markup_MultiBindingExtensionBase_ValidationRules.htm)|  
## __Методы
[ProvideValue](M_Tessa_UI_Markup_BindingBaseExtensionBase_ProvideValue.htm)|  
(Унаследован от
[BindingBaseExtensionBase](T_Tessa_UI_Markup_BindingBaseExtensionBase.htm))  
---|---  
[SetBinding](M_Tessa_UI_Markup_BindingBaseExtensionBase_SetBinding.htm)|  
(Унаследован от
[BindingBaseExtensionBase](T_Tessa_UI_Markup_BindingBaseExtensionBase.htm))  
##  __См. также
#### Ссылки
[Tessa.UI.Markup - пространство имён](N_Tessa_UI_Markup.htm)
