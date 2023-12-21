# ValueExtension<T> \- класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Markup](N_Tessa_UI_Markup.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ValueExtension<T> : MarkupExtension
VB __Копировать
     Public MustInherit Class ValueExtension(Of T)
    	Inherits MarkupExtension
C++ __Копировать
    generic<typename T>
    public ref class ValueExtension abstract : public MarkupExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type ValueExtension<'T> = 
        class
            inherit MarkupExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[MarkupExtension](https://learn.microsoft.com/dotnet/api/system.windows.markup.markupextension) __ ValueExtension<T>
Derived
[Tessa.UI.Markup.BooleanExtension](T_Tessa_UI_Markup_BooleanExtension.htm)
[Tessa.UI.Markup.DoubleExtension](T_Tessa_UI_Markup_DoubleExtension.htm)
[Tessa.UI.Markup.IntExtension](T_Tessa_UI_Markup_IntExtension.htm)
[Tessa.UI.Markup.VisibilityExtension](T_Tessa_UI_Markup_VisibilityExtension.htm)
#### Параметры типа
T
##  __Конструкторы
[ValueExtension<T>()](M_Tessa_UI_Markup_ValueExtension_1__ctor.htm)|
Инициализирует новый экземпляр класса ValueExtension<T>  
---|---  
[ValueExtension<T>(T)](M_Tessa_UI_Markup_ValueExtension_1__ctor_1.htm)|
Инициализирует новый экземпляр класса ValueExtension<T>  
##  __Свойства
[Value](P_Tessa_UI_Markup_ValueExtension_1_Value.htm)|  
---|---  
## __Методы
[BoxValue](M_Tessa_UI_Markup_ValueExtension_1_BoxValue.htm)|  
---|---  
[ProvideValue](M_Tessa_UI_Markup_ValueExtension_1_ProvideValue.htm)|  
(Переопределяет
[MarkupExtension.ProvideValue(IServiceProvider)](https://learn.microsoft.com/dotnet/api/system.windows.markup.markupextension.providevalue#system-
windows-markup-markupextension-providevalue\(system-iserviceprovider\)))  
##  __См. также
#### Ссылки
[Tessa.UI.Markup - пространство имён](N_Tessa_UI_Markup.htm)
