# NumberTypeDescriptor - класс
Тип номера и дополнительная информация по способу его использования.
Наследники класса могут определять такую информация в строго типизированных
свойствах, в остальных случаях она указывается в
[Info](P_Tessa_Cards_Numbers_NumberTypeDescriptor_Info.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public class NumberTypeDescriptor : IEquatable<NumberType>, 
    	IEquatable<NumberTypeDescriptor>, ISealable
VB __Копировать
    <SerializableAttribute>
    Public Class NumberTypeDescriptor
    	Implements IEquatable(Of NumberType), IEquatable(Of NumberTypeDescriptor), 
    	ISealable
C++ __Копировать
    [SerializableAttribute]
    public ref class NumberTypeDescriptor : IEquatable<NumberType^>, 
    	IEquatable<NumberTypeDescriptor^>, ISealable
F# __Копировать
     [<SerializableAttribute>]
    type NumberTypeDescriptor = 
        class
            interface IEquatable<NumberType>
            interface IEquatable<NumberTypeDescriptor>
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberTypeDescriptor
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[NumberType](T_Tessa_Cards_Numbers_NumberType.htm)>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<NumberTypeDescriptor>, [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Заметки
Объект можно непосредственно сравнивать с
[NumberType](T_Tessa_Cards_Numbers_NumberType.htm). При сравнивании
экземпляров этого класса по умолчанию сравниваются только их типы и значения
свойств [Type](P_Tessa_Cards_Numbers_NumberTypeDescriptor_Type.htm). Для
сравнения по другим полям используйте перегрузку соответствующего метода
сравнения
[Equals(NumberTypeDescriptor)](M_Tessa_Cards_Numbers_NumberTypeDescriptor_Equals_2.htm).
## __Конструкторы
[NumberTypeDescriptor](M_Tessa_Cards_Numbers_NumberTypeDescriptor__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Info](P_Tessa_Cards_Numbers_NumberTypeDescriptor_Info.htm)|  Информация по
особенностям использования типа номера.  
---|---  
[IsSealed](P_Tessa_Cards_Numbers_NumberTypeDescriptor_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
[Type](P_Tessa_Cards_Numbers_NumberTypeDescriptor_Type.htm)|  Тип номера.  
## __Методы
[Equals(NumberType)](M_Tessa_Cards_Numbers_NumberTypeDescriptor_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
---|---  
[Equals(NumberTypeDescriptor)](M_Tessa_Cards_Numbers_NumberTypeDescriptor_Equals_2.htm)|
Сравнивает текущий объект с заданным.  
[Equals(Object)](M_Tessa_Cards_Numbers_NumberTypeDescriptor_Equals.htm)|
Сравнивает текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Cards_Numbers_NumberTypeDescriptor_GetHashCode.htm)|
Возвращает хеш-код объекта.  
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
[Seal](M_Tessa_Cards_Numbers_NumberTypeDescriptor_Seal.htm)| Защищает объект
от изменений.  
[SealInternal](M_Tessa_Cards_Numbers_NumberTypeDescriptor_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[ToString](M_Tessa_Cards_Numbers_NumberTypeDescriptor_ToString.htm)|
Возвращает строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Операторы
[Equality(NumberType,
NumberTypeDescriptor)](M_Tessa_Cards_Numbers_NumberTypeDescriptor_op_Equality.htm)|
Сравнивает заданные значения на равенство.  
---|---  
[Equality(NumberTypeDescriptor,
NumberType)](M_Tessa_Cards_Numbers_NumberTypeDescriptor_op_Equality_1.htm)|
Сравнивает заданные значения на равенство.  
[Implicit(NumberType to
NumberTypeDescriptor)](M_Tessa_Cards_Numbers_NumberTypeDescriptor_op_Implicit.htm)|
Оператор, преобразующий объект
[NumberType](T_Tessa_Cards_Numbers_NumberType.htm) к объекту
NumberTypeDescriptor. Возвращённый объект защищён от изменений.  
[Inequality(NumberType,
NumberTypeDescriptor)](M_Tessa_Cards_Numbers_NumberTypeDescriptor_op_Inequality.htm)|
Сравнивает заданные значения на неравенство.  
[Inequality(NumberTypeDescriptor,
NumberType)](M_Tessa_Cards_Numbers_NumberTypeDescriptor_op_Inequality_1.htm)|
Сравнивает заданные значения на неравенство.  
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
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
