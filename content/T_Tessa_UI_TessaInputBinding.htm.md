# TessaInputBinding - класс
Привязка команды к жесту (нажатию клавиши или клику мыши).
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TessaInputBinding : IInputBinding, 
    	IEquatable<IInputBinding>, IEquatable<InputBinding>
VB __Копировать
     Public NotInheritable Class TessaInputBinding
    	Implements IInputBinding, IEquatable(Of IInputBinding), 
    	IEquatable(Of InputBinding)
C++ __Копировать
     public ref class TessaInputBinding sealed : IInputBinding, 
    	IEquatable<IInputBinding^>, IEquatable<InputBinding^>
F# __Копировать
     [<SealedAttribute>]
    type TessaInputBinding = 
        class
            interface IInputBinding
            interface IEquatable<IInputBinding>
            interface IEquatable<InputBinding>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaInputBinding
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[IInputBinding](T_Tessa_UI_IInputBinding.htm)>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[InputBinding](https://learn.microsoft.com/dotnet/api/system.windows.input.inputbinding)>, [IInputBinding](T_Tessa_UI_IInputBinding.htm)
##  __Конструкторы
[TessaInputBinding](M_Tessa_UI_TessaInputBinding__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Command](P_Tessa_UI_TessaInputBinding_Command.htm)| Команда.  
---|---  
[Gesture](P_Tessa_UI_TessaInputBinding_Gesture.htm)| Жест, связанный с
командой. Обычно нажатие клавиши или клик мыши.  
##  __Методы
[Equals(IInputBinding)](M_Tessa_UI_TessaInputBinding_Equals_2.htm)| Сравнивает
текущий объект с заданным.  
---|---  
[Equals(InputBinding)](M_Tessa_UI_TessaInputBinding_Equals_1.htm)| Сравнивает
текущий объект с заданным.  
[Equals(Object)](M_Tessa_UI_TessaInputBinding_Equals.htm)| Сравнивает текущий
объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_UI_TessaInputBinding_GetHashCode.htm)| Возвращает хеш-
код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[CreateWpfBinding](M_Tessa_UI_UIExtensions_CreateWpfBinding.htm)|  Создаёт
объект привязки
[InputBinding](https://learn.microsoft.com/dotnet/api/system.windows.input.inputbinding)
для использования в WPF. Вызывайте в потоке диспетчера WPF.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
