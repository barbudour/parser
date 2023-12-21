# TreePropertyGroupDescription - класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Data](N_Tessa_UI_Data.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class TreePropertyGroupDescription : TreeGroupDescription
VB __Копировать
     Public Class TreePropertyGroupDescription
    	Inherits TreeGroupDescription
C++ __Копировать
     public ref class TreePropertyGroupDescription : public TreeGroupDescription
F# __Копировать
     type TreePropertyGroupDescription = 
        class
            inherit TreeGroupDescription
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[GroupDescription](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription) __[TreeGroupDescription](T_Tessa_UI_Data_TreeGroupDescription.htm) __ TreePropertyGroupDescription
##  __Конструкторы
[TreePropertyGroupDescription()](M_Tessa_UI_Data_TreePropertyGroupDescription__ctor.htm)|
Инициализирует новый экземпляр класса TreePropertyGroupDescription  
---|---  
[TreePropertyGroupDescription(Object)](M_Tessa_UI_Data_TreePropertyGroupDescription__ctor_1.htm)|
Инициализирует новый экземпляр класса TreePropertyGroupDescription  
[TreePropertyGroupDescription(String)](M_Tessa_UI_Data_TreePropertyGroupDescription__ctor_5.htm)|
Инициализирует новый экземпляр класса TreePropertyGroupDescription  
[TreePropertyGroupDescription(TreeGroupDescription[])](M_Tessa_UI_Data_TreePropertyGroupDescription__ctor_7.htm)|
Инициализирует новый экземпляр класса TreePropertyGroupDescription  
[TreePropertyGroupDescription(Object,
String)](M_Tessa_UI_Data_TreePropertyGroupDescription__ctor_2.htm)|
Инициализирует новый экземпляр класса TreePropertyGroupDescription  
[TreePropertyGroupDescription(Object,
TreeGroupDescription[])](M_Tessa_UI_Data_TreePropertyGroupDescription__ctor_4.htm)|
Инициализирует новый экземпляр класса TreePropertyGroupDescription  
[TreePropertyGroupDescription(String,
TreeGroupDescription[])](M_Tessa_UI_Data_TreePropertyGroupDescription__ctor_6.htm)|
Инициализирует новый экземпляр класса TreePropertyGroupDescription  
[TreePropertyGroupDescription(Object, String,
TreeGroupDescription[])](M_Tessa_UI_Data_TreePropertyGroupDescription__ctor_3.htm)|
Инициализирует новый экземпляр класса TreePropertyGroupDescription  
##  __Свойства
[Children](P_Tessa_UI_Data_TreeGroupDescription_Children.htm)|  
(Унаследован от
[TreeGroupDescription](T_Tessa_UI_Data_TreeGroupDescription.htm))  
---|---  
[Converter](P_Tessa_UI_Data_TreePropertyGroupDescription_Converter.htm)|  
[CustomSort](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.customsort#system-
componentmodel-groupdescription-customsort)| Gets or sets a custom comparer
that sorts groups using an object that implements
[IComparer](https://learn.microsoft.com/dotnet/api/system.collections.icomparer).  
(Унаследован от
[GroupDescription](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription))  
[GroupName](P_Tessa_UI_Data_TreeGroupDescription_GroupName.htm)|  
(Унаследован от
[TreeGroupDescription](T_Tessa_UI_Data_TreeGroupDescription.htm))  
[GroupNames](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.groupnames#system-
componentmodel-groupdescription-groupnames)| Gets the collection of names that
are used to initialize a group with a set of subgroups with the given names.  
(Унаследован от
[GroupDescription](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription))  
[PropertyName](P_Tessa_UI_Data_TreePropertyGroupDescription_PropertyName.htm)|  
[SortDescriptions](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.sortdescriptions#system-
componentmodel-groupdescription-sortdescriptions)| Gets the collection of sort
criteria in which to sort the groups.  
(Унаследован от
[GroupDescription](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription))  
[StringComparison](P_Tessa_UI_Data_TreePropertyGroupDescription_StringComparison.htm)|  
## __Методы
[GroupNameFromItem(Object, Int32,
CultureInfo)](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.groupnamefromitem#system-
componentmodel-groupdescription-groupnamefromitem\(system-object-system-
int32-system-globalization-cultureinfo\))| Returns the group name(s) for the
given item.  
(Унаследован от
[GroupDescription](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription))  
---|---  
[GroupNameFromItem(Object, Int32,
CultureInfo)](M_Tessa_UI_Data_TreePropertyGroupDescription_GroupNameFromItem.htm)|  
[NamesMatch](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.namesmatch#system-
componentmodel-groupdescription-namesmatch\(system-object-system-object\))|
Returns a value that indicates whether the group name and the item name match
such that the item belongs to the group.  
(Унаследован от
[GroupDescription](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription))  
[OnPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.onpropertychanged#system-
componentmodel-groupdescription-onpropertychanged\(system-componentmodel-
propertychangedeventargs\))| Raises the
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.propertychanged)
event.  
(Унаследован от
[GroupDescription](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription))  
[ShouldSerializeChildren](M_Tessa_UI_Data_TreeGroupDescription_ShouldSerializeChildren.htm)|  
(Унаследован от
[TreeGroupDescription](T_Tessa_UI_Data_TreeGroupDescription.htm))  
[ShouldSerializeGroupNames](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.shouldserializegroupnames#system-
componentmodel-groupdescription-shouldserializegroupnames)| Returns whether
serialization processes should serialize the effective value of the
[GroupNames](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.groupnames#system-
componentmodel-groupdescription-groupnames) property on instances of this
class.  
(Унаследован от
[GroupDescription](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription))  
[ShouldSerializeSortDescriptions](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.shouldserializesortdescriptions#system-
componentmodel-groupdescription-shouldserializesortdescriptions)| Returns
whether serialization processes should serialize the effective value of the
[SortDescriptions](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.sortdescriptions#system-
componentmodel-groupdescription-sortdescriptions) property on instances of
this class.  
(Унаследован от
[GroupDescription](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription))  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[GroupDescription](https://learn.microsoft.com/dotnet/api/system.componentmodel.groupdescription))  
---|---  
##  __См. также
#### Ссылки
[Tessa.UI.Data - пространство имён](N_Tessa_UI_Data.htm)
