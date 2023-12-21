# Tessa.Properties.Resharper - пространство имён
Аннотации (атрибуты), используемые в Resharper (например, [NotNull] или
[UsedImplicitly]).
##  __Классы
[AspMvcActionAttribute](T_Tessa_Properties_Resharper_AspMvcActionAttribute.htm)|
ASP.NET MVC attribute. If applied to a parameter, indicates that the parameter
is an MVC action. If applied to a method, the MVC action name is calculated
implicitly from the context. Use this attribute for custom wrappers similar to
System.Web.Mvc.Html.ChildActionExtensions.RenderAction(HtmlHelper, String)"  
---|---  
[AspMvcActionSelectorAttribute](T_Tessa_Properties_Resharper_AspMvcActionSelectorAttribute.htm)|
ASP.NET MVC attribute. When applied to a parameter of an attribute, indicates
that this parameter is an MVC action name.  
[AspMvcAreaAttribute](T_Tessa_Properties_Resharper_AspMvcAreaAttribute.htm)|
ASP.NET MVC attribute. Indicates that a parameter is an MVC araa. Use this
attribute for custom wrappers similar to
System.Web.Mvc.Html.ChildActionExtensions.RenderAction(HtmlHelper, String)"  
[AspMvcControllerAttribute](T_Tessa_Properties_Resharper_AspMvcControllerAttribute.htm)|
ASP.NET MVC attribute. If applied to a parameter, indicates that the parameter
is an MVC controller. If applied to a method, the MVC controller name is
calculated implicitly from the context. Use this attribute for custom wrappers
similar to System.Web.Mvc.Html.ChildActionExtensions.RenderAction(HtmlHelper,
String, String)"  
[AspMvcDisplayTemplateAttribute](T_Tessa_Properties_Resharper_AspMvcDisplayTemplateAttribute.htm)|
ASP.NET MVC attribute. Indicates that a parameter is an MVC display template.
Use this attribute for custom wrappers similar to
System.Web.Mvc.Html.DisplayExtensions.DisplayForModel(HtmlHelper, String)"  
[AspMvcEditorTemplateAttribute](T_Tessa_Properties_Resharper_AspMvcEditorTemplateAttribute.htm)|
ASP.NET MVC attribute. Indicates that a parameter is an MVC editor template.
Use this attribute for custom wrappers similar to
System.Web.Mvc.Html.EditorExtensions.EditorForModel(HtmlHelper, String)"  
[AspMvcMasterAttribute](T_Tessa_Properties_Resharper_AspMvcMasterAttribute.htm)|
ASP.NET MVC attribute. Indicates that a parameter is an MVC Master. Use this
attribute for custom wrappers similar to
System.Web.Mvc.Controller.View(String, String)"  
[AspMvcModelTypeAttribute](T_Tessa_Properties_Resharper_AspMvcModelTypeAttribute.htm)|
ASP.NET MVC attribute. Indicates that a parameter is an MVC model type. Use
this attribute for custom wrappers similar to
cref="System.Web.Mvc.Controller.View(String, Object)"  
[AspMvcPartialViewAttribute](T_Tessa_Properties_Resharper_AspMvcPartialViewAttribute.htm)|
ASP.NET MVC attribute. If applied to a parameter, indicates that the parameter
is an MVC partial view. If applied to a method, the MVC partial view name is
calculated implicitly from the context. Use this attribute for custom wrappers
similar to
System.Web.Mvc.Html.RenderPartialExtensions.RenderPartial(HtmlHelper, String)"  
[AspMvcSupressViewErrorAttribute](T_Tessa_Properties_Resharper_AspMvcSupressViewErrorAttribute.htm)|
ASP.NET MVC attribute. Allows disabling all inspections for MVC views within a
class or a method.  
[AspMvcViewAttribute](T_Tessa_Properties_Resharper_AspMvcViewAttribute.htm)|
ASP.NET MVC attribute. If applied to a parameter, indicates that the parameter
is an MVC view. If applied to a method, the MVC view name is calculated
implicitly from the context. Use this attribute for custom wrappers similar to
System.Web.Mvc.Controller.View(Object)"  
[BaseTypeRequiredAttribute](T_Tessa_Properties_Resharper_BaseTypeRequiredAttribute.htm)|
When applied to a target attribute, specifies a requirement for any type
marked with the target attribute to implement or inherit specific type or
types.  
[CanBeNullAttribute](T_Tessa_Properties_Resharper_CanBeNullAttribute.htm)|
Indicates that the value of the marked element could be null sometimes, so the
check for null is necessary before its usage.  
[CannotApplyEqualityOperatorAttribute](T_Tessa_Properties_Resharper_CannotApplyEqualityOperatorAttribute.htm)|
Indicates that the value of the marked type (or its derivatives) cannot be
compared using '==' or '!=' operators and Equals() should be used instead.
However, using '==' or '!=' for comparison with null is always permitted.  
[ContractAnnotationAttribute](T_Tessa_Properties_Resharper_ContractAnnotationAttribute.htm)|
Describes dependency between method input and output.  
[InstantHandleAttribute](T_Tessa_Properties_Resharper_InstantHandleAttribute.htm)|
Tells code analysis engine if the parameter is completely handled when the
invoked method is on stack. If the parameter is a delegate, indicates that
delegate is executed while the method is executed. If the parameter is an
enumerable, indicates that it is enumerated while the method is executed.  
[InvokerParameterNameAttribute](T_Tessa_Properties_Resharper_InvokerParameterNameAttribute.htm)|
Indicates that the function argument should be string literal and match one of
the parameters of the caller function. For example, ReSharper annotates the
parameter of
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception).  
[LocalizationRequiredAttribute](T_Tessa_Properties_Resharper_LocalizationRequiredAttribute.htm)|
Indicates that marked element should be localized or not.  
[MeansImplicitUseAttribute](T_Tessa_Properties_Resharper_MeansImplicitUseAttribute.htm)|
Should be used on attributes and causes ReSharper to not mark symbols marked
with such attributes as unused (as well as by other usage inspections)  
[NotifyPropertyChangedInvocatorAttribute](T_Tessa_Properties_Resharper_NotifyPropertyChangedInvocatorAttribute.htm)|
Indicates that the method is contained in a type that implements
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
interface and this method is used to notify that some property value changed.  
[NotNullAttribute](T_Tessa_Properties_Resharper_NotNullAttribute.htm)|
Indicates that the value of the marked element could never be null  
[PathReferenceAttribute](T_Tessa_Properties_Resharper_PathReferenceAttribute.htm)|
Indicates that a parameter is a path to a file or a folder within a web
project. Path can be relative or absolute, starting from web root (~).  
[PublicAPIAttribute](T_Tessa_Properties_Resharper_PublicAPIAttribute.htm)|
This attribute is intended to mark publicly available API which should not be
removed and so is treated as used.  
[PureAttribute](T_Tessa_Properties_Resharper_PureAttribute.htm)|  Indicates
that a method does not make any observable state changes. The same as
[PureAttribute](https://learn.microsoft.com/dotnet/api/system.diagnostics.contracts.pureattribute)  
[RazorSectionAttribute](T_Tessa_Properties_Resharper_RazorSectionAttribute.htm)|
Razor attribute. Indicates that a parameter or a method is a Razor section.
Use this attribute for custom wrappers similar to
System.Web.WebPages.WebPageBase.RenderSection(String)"  
[StringFormatMethodAttribute](T_Tessa_Properties_Resharper_StringFormatMethodAttribute.htm)|
Indicates that the marked method builds string by format pattern and
(optional) arguments. Parameter, which contains format string, should be given
in constructor. The format string should be in [Format(IFormatProvider,
String,
Object[])](https://learn.microsoft.com/dotnet/api/system.string.format#system-
string-format\(system-iformatprovider-system-string-system-object\(\)\)) -like
form  
[UsedImplicitlyAttribute](T_Tessa_Properties_Resharper_UsedImplicitlyAttribute.htm)|
Indicates that the marked symbol is used implicitly (e.g. via reflection, in
external library), so this symbol will not be marked as unused (as well as by
other usage inspections)  
## __Перечисления
[ImplicitUseKindFlags](T_Tessa_Properties_Resharper_ImplicitUseKindFlags.htm)|
The implicit use kind flags.  
---|---  
[ImplicitUseTargetFlags](T_Tessa_Properties_Resharper_ImplicitUseTargetFlags.htm)|
Specify what is considered used implicitly when marked with
[MeansImplicitUseAttribute](T_Tessa_Properties_Resharper_MeansImplicitUseAttribute.htm)
or
[UsedImplicitlyAttribute](T_Tessa_Properties_Resharper_UsedImplicitlyAttribute.htm)
