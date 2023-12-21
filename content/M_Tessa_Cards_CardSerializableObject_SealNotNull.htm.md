# CardSerializableObject.SealNotNull - метод
Защищает от изменений заданный объект, если он не равен null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void SealNotNull(
    	[CanBeNullAttribute] ISealable obj
    )
VB __Копировать
     Protected Shared Sub SealNotNull ( 
    	<CanBeNullAttribute> obj As ISealable
    )
C++ __Копировать
     protected:
    static void SealNotNull(
    	[CanBeNullAttribute] ISealable^ obj
    )
F# __Копировать
     static member SealNotNull : 
            [<CanBeNullAttribute>] obj : ISealable -> unit 
#### Параметры
obj [ISealable](T_Tessa_Platform_ISealable.htm)
    Защищаемый от изменений объект или null, если объект отсутствует.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
