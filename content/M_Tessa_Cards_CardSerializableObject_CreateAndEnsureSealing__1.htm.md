# CardSerializableObject.CreateAndEnsureSealing<T> \- метод
Создаёт объект типа T посредством конструктора по умолчанию и защищает его от
изменений, если текущий объект также защищён от изменений.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected T CreateAndEnsureSealing<T>()
    where T : new(), ISealable
VB __Копировать
     Protected Function CreateAndEnsureSealing(Of T As {New, ISealable}) As T
C++ __Копировать
     protected:
    generic<typename T>
    where T : gcnew(), ISealable
    T CreateAndEnsureSealing()
F# __Копировать
     member CreateAndEnsureSealing : unit -> 'T  when 'T : new() and ISealable
#### Параметры типа
T
     Тип создаваемого объекта, который должен иметь конструктор по умолчанию и реализовывать интерфейс [Tessa.Platform.ISealable]. 
#### Возвращаемое значение
T  
Созданный экземпляр типа T, который может быть защищён от изменений.
## __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
