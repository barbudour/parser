# BindableDynamicObject - класс
Динамический объект с привзякой данных
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class BindableDynamicObject : DynamicObject, 
    	INotifyPropertyChanged, IGetPropertyValue
VB __Копировать
     Public Class BindableDynamicObject
    	Inherits DynamicObject
    	Implements INotifyPropertyChanged, IGetPropertyValue
C++ __Копировать
     public ref class BindableDynamicObject : public DynamicObject, 
    	INotifyPropertyChanged, IGetPropertyValue
F# __Копировать
     type BindableDynamicObject = 
        class
            inherit DynamicObject
            interface INotifyPropertyChanged
            interface IGetPropertyValue
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject) __ BindableDynamicObject
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IGetPropertyValue](T_Tessa_UI_IGetPropertyValue.htm)
##  __Конструкторы
[BindableDynamicObject(IDictionary<String,
Object>)](M_Tessa_UI_BindableDynamicObject__ctor.htm)|  Initializes a new
instance of the BindableDynamicObject class.  
---|---  
[BindableDynamicObject(IEnumerable<Object>,
IList<Object>)](M_Tessa_UI_BindableDynamicObject__ctor_1.htm)|  Initializes a
new instance of the BindableDynamicObject class. Позволяет производным типам
инициализировать новый экземпляр типа
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject).  
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
[GetDynamicMemberNames](M_Tessa_UI_BindableDynamicObject_GetDynamicMemberNames.htm)|
Возвращает перечисление имен всех динамических членов.  
(Переопределяет
[DynamicObject.GetDynamicMemberNames()](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.getdynamicmembernames#system-
dynamic-dynamicobject-getdynamicmembernames))  
[GetFirstStringValueByPrefix](M_Tessa_UI_BindableDynamicObject_GetFirstStringValueByPrefix.htm)|
Возвращает значение первого строкового поля с имененм начинающимся с префикса  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMetaObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.getmetaobject#system-
dynamic-dynamicobject-getmetaobject\(system-linq-expressions-expression\))|
Provides a
[DynamicMetaObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicmetaobject)
that dispatches to the dynamic virtual methods. The object can be encapsulated
inside another
[DynamicMetaObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicmetaobject)
to provide custom behavior for individual actions. This method supports the
Dynamic Language Runtime infrastructure for language implementers and it is
not intended to be used directly from your code.  
(Унаследован от
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject))  
[GetPropertyNames](M_Tessa_UI_BindableDynamicObject_GetPropertyNames.htm)|
Возвращает список имен свойств  
[GetPropertyNamesByPrefix](M_Tessa_UI_BindableDynamicObject_GetPropertyNamesByPrefix.htm)|
Возвращает список имен полей начинающихся с префикса  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetValueID](M_Tessa_UI_BindableDynamicObject_GetValueID.htm)|  Возвращает
значение свойства по его префиксу. Возвращаемое значение формируется из
префикса и ID или RowID в зависимости от того что существует.  
[GetValuesByPrefix](M_Tessa_UI_BindableDynamicObject_GetValuesByPrefix.htm)|
Возвращает список значений полей начинающихся с имени префикса  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnPropertyChanged](M_Tessa_UI_BindableDynamicObject_OnPropertyChanged.htm)|
The on property changed.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryBinaryOperation](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trybinaryoperation#system-
dynamic-dynamicobject-trybinaryoperation\(system-dynamic-
binaryoperationbinder-system-object-system-object@\))| Provides implementation
for binary operations. Classes derived from the
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject)
class can override this method to specify dynamic behavior for operations such
as addition and multiplication.  
(Унаследован от
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject))  
[TryConvert](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.tryconvert#system-
dynamic-dynamicobject-tryconvert\(system-dynamic-convertbinder-system-
object@\))| Provides implementation for type conversion operations. Classes
derived from the
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject)
class can override this method to specify dynamic behavior for operations that
convert an object from one type to another.  
(Унаследован от
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject))  
[TryCreateInstance](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trycreateinstance#system-
dynamic-dynamicobject-trycreateinstance\(system-dynamic-createinstancebinder-
system-object\(\)-system-object@\))| Provides the implementation for
operations that initialize a new instance of a dynamic object. This method is
not intended for use in C# or Visual Basic.  
(Унаследован от
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject))  
[TryDeleteIndex](M_Tessa_UI_BindableDynamicObject_TryDeleteIndex.htm)|
Предоставляет реализацию для операций, удаляющих объект по индексу.Этот метод
не предназначен для использования в C# или Visual Basic.  
(Переопределяет [DynamicObject.TryDeleteIndex(DeleteIndexBinder,
Object[])](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trydeleteindex#system-
dynamic-dynamicobject-trydeleteindex\(system-dynamic-deleteindexbinder-system-
object\(\)\)))  
[TryDeleteMember](M_Tessa_UI_BindableDynamicObject_TryDeleteMember.htm)|
Предоставляет реализацию для операций, удаляющих элемент объекта.Этот метод не
предназначен для использования в C# или Visual Basic.  
(Переопределяет
[DynamicObject.TryDeleteMember(DeleteMemberBinder)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trydeletemember#system-
dynamic-dynamicobject-trydeletemember\(system-dynamic-deletememberbinder\)))  
[TryGetIndex](M_Tessa_UI_BindableDynamicObject_TryGetIndex.htm)|
Предоставляет реализацию для операций, получающих значение по индексу.Классы,
производные от класса
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject)
, могут переопределять этот метод, чтобы задать динамическое поведение для
операций индексации.  
(Переопределяет [DynamicObject.TryGetIndex(GetIndexBinder, Object[],
Object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trygetindex#system-
dynamic-dynamicobject-trygetindex\(system-dynamic-getindexbinder-system-
object\(\)-system-object@\)))  
[TryGetMember](M_Tessa_UI_BindableDynamicObject_TryGetMember.htm)|
Предоставляет реализацию для операций, получающих значения членов.Классы,
производные от класса
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject)
, могут переопределять этот метод, чтобы задать динамическое поведение для
таких операций, как получение значения свойства.  
(Переопределяет [DynamicObject.TryGetMember(GetMemberBinder,
Object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trygetmember#system-
dynamic-dynamicobject-trygetmember\(system-dynamic-getmemberbinder-system-
object@\)))  
[TryInvoke](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.tryinvoke#system-
dynamic-dynamicobject-tryinvoke\(system-dynamic-invokebinder-system-
object\(\)-system-object@\))| Provides the implementation for operations that
invoke an object. Classes derived from the
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject)
class can override this method to specify dynamic behavior for operations such
as invoking an object or a delegate.  
(Унаследован от
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject))  
[TryInvokeMember](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.tryinvokemember#system-
dynamic-dynamicobject-tryinvokemember\(system-dynamic-invokememberbinder-
system-object\(\)-system-object@\))| Provides the implementation for
operations that invoke a member. Classes derived from the
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject)
class can override this method to specify dynamic behavior for operations such
as calling a method.  
(Унаследован от
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject))  
[TrySetIndex](M_Tessa_UI_BindableDynamicObject_TrySetIndex.htm)|
Предоставляет реализацию для операций, задающих значение по индексу.Классы,
производные от класса
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject)
, могут переопределять этот метод, чтобы задать динамическое поведение для
операций, осуществляющих доступ к объектам по заданному индексу.  
(Переопределяет [DynamicObject.TrySetIndex(SetIndexBinder, Object[],
Object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trysetindex#system-
dynamic-dynamicobject-trysetindex\(system-dynamic-setindexbinder-system-
object\(\)-system-object\)))  
[TrySetMember](M_Tessa_UI_BindableDynamicObject_TrySetMember.htm)|
Предоставляет реализацию для операций, задающих значения членов.Классы,
производные от класса
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject)
, могут переопределять этот метод, чтобы задать динамическое поведение для
таких операций, как задание значения свойства.  
(Переопределяет [DynamicObject.TrySetMember(SetMemberBinder,
Object)](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.trysetmember#system-
dynamic-dynamicobject-trysetmember\(system-dynamic-setmemberbinder-system-
object\)))  
[TryUnaryOperation](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject.tryunaryoperation#system-
dynamic-dynamicobject-tryunaryoperation\(system-dynamic-unaryoperationbinder-
system-object@\))| Provides implementation for unary operations. Classes
derived from the
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject)
class can override this method to specify dynamic behavior for operations such
as negation, increment, or decrement.  
(Унаследован от
[DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject))  
##  __События
[PropertyChanged](E_Tessa_UI_BindableDynamicObject_PropertyChanged.htm)|  The
property changed.  
---|---  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
